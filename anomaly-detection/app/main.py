from fastapi import FastAPI

from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_logging
from app.routers.health import router as health_router
from app.routers.detection import router as detection_router
from app.routers.history import router as history_router

logger = configure_logging()

app = FastAPI(
    title=settings.app_name,
    description="Production Cloud-Native Anomaly Detection Platform",
    version=settings.app_version,
)

app.include_router(health_router)
app.include_router(detection_router)
app.include_router(history_router)

register_exception_handlers(app)


@app.get("/")
async def root():
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "status": "running",
    }


logger.info("KRONOS service started successfully.")