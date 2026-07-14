from fastapi import FastAPI

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
