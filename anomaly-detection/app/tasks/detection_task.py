from datetime import datetime
from pathlib import Path

from app.workers.celery_app import celery
from app.core.database import SessionLocal
from app.repositories.job_repository import JobRepository
from app.services.csv_service import CSVService


@celery.task(name="detect_anomalies")
def detect_anomalies_task(
    job_id: str,
    filename: str,
):
    """
    Background task for processing uploaded CSV files.
    """

    import asyncio

    async def process():
        db = SessionLocal()

        try:
            repository = JobRepository(db)

            job = await repository.get_by_task_id(job_id)

            if job is None:
                return

            job.status = "RUNNING"
            await repository.update(job)

            csv_service = CSVService()

            filepath = Path("app/storage/uploads") / filename

            dataframe = csv_service.load_saved_csv(filepath)

            # Detection logic will be added in Part 3.
            print(dataframe.head())

            job.status = "COMPLETED"
            job.completed_at = datetime.utcnow()

            await repository.update(job)

        except Exception as exc:
            job = await repository.get_by_task_id(job_id)

            if job:
                job.status = "FAILED"
                job.error_message = str(exc)
                job.completed_at = datetime.utcnow()

                await repository.update(job)

        finally:
            await db.close()

    asyncio.run(process())