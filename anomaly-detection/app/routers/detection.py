import pandas as pd
from fastapi import APIRouter

from app.models.detection import DetectionRequest
from app.services.detector_service import DetectorService

router = APIRouter(
    prefix="/detect",
    tags=["Detection"],
)

service = DetectorService()


@router.post("/")
async def detect(request: DetectionRequest):
    """
    Run anomaly detection on the supplied time-series values.
    """

    dataframe = pd.DataFrame(
        {
            request.column_name: request.values
        }
    )

    result = service.run_detection(
        dataframe=dataframe,
        column_name=request.column_name,
    )

    report = result["report"]

    return {
        "status": "success",
        "total_records": len(report),
        "confirmed_anomalies": result["total_anomalies"],
        "report": report.to_dict(orient="records"),
    }