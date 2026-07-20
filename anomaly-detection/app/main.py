"""
KRONOS FastAPI Application - Main entry point.
"""

import time

from fastapi import FastAPI, Request
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from starlette.responses import Response

from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_logging
from app.core.monitoring import (
    ACTIVE_REQUESTS,
    ERROR_COUNT,
    REQUEST_COUNT,
    REQUEST_LATENCY,
)
from app.routers.auth import router as auth_router
from app.routers.detection import router as detection_router
from app.routers.health import router as health_router
from app.routers.history import router as history_router
from app.routers.jobs import router as jobs_router
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


@app.middleware("http")
async def prometheus_middleware(request: Request, call_next):
    """
    Collect Prometheus metrics for every request.
    """

    ACTIVE_REQUESTS.inc()

    start_time = time.perf_counter()

    try:
        response = await call_next(request)

        REQUEST_COUNT.labels(
            request.method,
            request.url.path,
            response.status_code,
        ).inc()

        return response

    except Exception:
        ERROR_COUNT.labels(
            request.method,
            request.url.path,
        ).inc()
        raise

    finally:
        duration = time.perf_counter() - start_time

        REQUEST_LATENCY.labels(
            request.method,
            request.url.path,
        ).observe(duration)

        ACTIVE_REQUESTS.dec()


@app.get("/metrics", include_in_schema=False)
async def metrics():
    """
    Prometheus metrics endpoint.
    """

    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )


# Register routers
app.include_router(health_router)
app.include_router(detection_router)
app.include_router(history_router)
app.include_router(upload_router)
app.include_router(jobs_router)
app.include_router(auth_router)

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
