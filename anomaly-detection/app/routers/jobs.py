import uuid

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.db.job_history import JobHistory
from app.repositories.job_repository import JobRepository
from app.services.csv_service import CSVService

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)

csv_service = CSVService()


@router.post("/upload")
async def upload_job(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
):
    """
    Upload a CSV and create a pending background job.
    """

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is missing.",
        )

    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are supported.",
        )

    job_id = str(uuid.uuid4())

    saved_filename = f"{job_id}_{file.filename}"

    await csv_service.save_upload(
        file=file,
        filename=saved_filename,
    )

    repository = JobRepository(db)

    job = JobHistory(
        celery_task_id=job_id,
        filename=saved_filename,
        status="PENDING",
    )

    await repository.save(job)

    return {
        "job_id": job_id,
        "status": "PENDING",
        "filename": saved_filename,
    }