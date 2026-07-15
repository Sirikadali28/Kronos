from fastapi import FastAPI

<<<<<<< HEAD
app = FastAPI(
    title="KRONOS",
    description="Cloud-Native Anomaly Detection Platform",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/")
def root():
    """
    Temporary root endpoint.
    This will be replaced with proper routers in later milestones.
    """
    return {
        "service": "KRONOS",
        "status": "running",
        "version": "2.0.0"
    }
=======
from app.core.config import settings
from app.core.logging import configure_logging
from app.routers.health import router as health_router
from app.routers.detection import router as detection_router
logger = configure_logging()

app = FastAPI(
    title=settings.app_name,
    description="Production Cloud-Native Anomaly Detection Platform",
    version=settings.app_version,
)

app.include_router(health_router)
app.include_router(detection_router)

@app.get("/")
async def root():
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "status": "running",
    }


logger.info("KRONOS service started successfully.")
>>>>>>> 5163675 (Phase 1 Milestone 4: Add FastAPI health and detection APIs)
