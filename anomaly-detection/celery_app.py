from app.core.config import settings

celery = Celery(
    "kronos",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
)
celery.autodiscover_tasks(
    ["app.tasks"]
)