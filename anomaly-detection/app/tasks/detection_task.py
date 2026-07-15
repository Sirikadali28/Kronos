from app.workers.celery_app import celery


@celery.task(name="detect_anomalies")
def detect_anomalies_task():
    """
    Temporary Celery task.
    """
    return {
        "status": "completed",
        "message": "Celery is working successfully."
    }