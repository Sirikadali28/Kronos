import time

import pandas as pd
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.db.detection_history import DetectionHistory
from app.db.user import User
from app.models.detection import DetectionRequest
from app.repositories.detection_repository import DetectionRepository
from app.services.detector_service import DetectorService

router = APIRouter(
    prefix="/detect",
    tags=["Detection"],
)

service = DetectorService()


@router.post("/")
async def detect(
    request: DetectionRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Run anomaly detection on the supplied time-series values.
    """

    start_time = time.perf_counter()

    dataframe = pd.DataFrame(
        {
            request.column_name: request.values
        }
    )

    result = service.run_detection(
        dataframe=dataframe,
        column_name=request.column_name,
    )

    execution_time = (time.perf_counter() - start_time) * 1000

    repository = DetectionRepository(db)

    history = DetectionHistory(
        records_processed=len(dataframe),
        anomaly_count=result["total_anomalies"],
        status="SUCCESS",
        execution_time_ms=execution_time,
        algorithm_version="1.0.0",
        report_path=None,
    )

    saved_history = await repository.save(history)

    report = result["report"]

    return {
        "status": "success",
        "history_id": str(saved_history.id),
        "total_records": len(report),
        "confirmed_anomalies": result["total_anomalies"],
        "execution_time_ms": round(execution_time, 2),
        "report": report.to_dict(orient="records"),
        "processed_by": current_user.email,
    }