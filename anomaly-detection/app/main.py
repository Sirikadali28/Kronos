"""
KRONOS FastAPI Application - Main entry point.
"""
from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import configure_logging
from app.core.exceptions import register_exception_handlers
from app.routers.health import router as health_router
from app.routers.detection import router as detection_router
from app.routers.history import router as history_router
from app.routers.upload import router as upload_router

# Configure logging
logger = configure_logging()

# Create FastAPI application instance
app = FastAPI(
    title=settings.app_name,
    description="Production Cloud-Native Anomaly Detection Platform",
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Register routers
app.include_router(health_router)
app.include_router(detection_router)
app.include_router(history_router)
app.include_router(upload_router)

# Register exception handlers
register_exception_handlers(app)


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint returning application information.
    """
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "status": "running",
    }


# Log startup
logger.info("KRONOS service initialized successfully.")

