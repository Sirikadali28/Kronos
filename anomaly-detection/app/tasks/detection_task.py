from datetime import datetime
from pathlib import Path
import asyncio

from app.core.database import SessionLocal
from app.repositories.job_repository import JobRepository
from app.services.csv_service import CSVService
from app.services.detector_service import DetectorService
from app.workers.celery_app import celery


@celery.task(name="detect_anomalies")
def detect_anomalies_task(
    job_id: str,
    filename: str,
):
    """
    Background task for processing uploaded CSV files.
    """

    async def process():
        db = SessionLocal()

        try:
            repository = JobRepository(db)

            job = await repository.get_by_task_id(job_id)

            if job is None:
                return

            # Mark job as running
            job.status = "RUNNING"
            await repository.update(job)

            # Load uploaded CSV
            csv_service = CSVService()

            upload_path = Path("app/storage/uploads")
            csv_path = upload_path / filename

            dataframe = csv_service.load_saved_csv(csv_path)

            # Create reports directory
            reports_path = Path("app/storage/reports")
            reports_path.mkdir(parents=True, exist_ok=True)

            report_file = reports_path / f"{job_id}.csv"

            # Run anomaly detection
            detector_service = DetectorService()

            detector_service.run_detection(
                dataframe=dataframe,
                column_name="value",
                output_file=str(report_file),
            )

            # Update job
            job.status = "COMPLETED"
            job.report_path = str(report_file)
            job.completed_at = datetime.utcnow()

            await repository.update(job)

        except Exception as exc:

            try:
                job = await repository.get_by_task_id(job_id)

                if job:
                    job.status = "FAILED"
                    job.error_message = str(exc)
                    job.completed_at = datetime.utcnow()

                    await repository.update(job)

            except Exception:
                pass

        finally:
            await db.close()

    asyncio.run(process())