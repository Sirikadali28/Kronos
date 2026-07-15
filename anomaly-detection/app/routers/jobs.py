from celery.result import AsyncResult
from fastapi import APIRouter

from app.tasks.detection_task import detect_anomalies_task
from app.workers.celery_app import celery

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.post("/test")
async def create_test_job():
    task = detect_anomalies_task.delay()

    return {
        "task_id": task.id,
        "status": "queued",
    }


@router.get("/{task_id}")
async def get_job_status(task_id: str):
    result = AsyncResult(task_id, app=celery)

    response = {
        "task_id": task_id,
        "status": result.status,
    }

    if result.successful():
        response["result"] = result.result

    return response