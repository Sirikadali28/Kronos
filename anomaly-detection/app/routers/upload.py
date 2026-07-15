from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.csv_service import CSVService
from app.services.detector_service import DetectorService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

csv_service = CSVService()
detector_service = DetectorService()


@router.post("/")
async def upload_csv(
    file: UploadFile = File(...),
    column_name: str = "value",
):
    """
    Upload a CSV file and run anomaly detection.
    """

    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed.",
        )

    dataframe = await csv_service.read_csv(file)

    if column_name not in dataframe.columns:
        raise HTTPException(
            status_code=400,
            detail=f"Column '{column_name}' not found.",
        )

    result = detector_service.run_detection(
        dataframe=dataframe,
        column_name=column_name,
    )

    report = result["report"]

    return {
        "status": "success",
        "rows": len(report),
        "confirmed_anomalies": result["total_anomalies"],
        "report": report.to_dict(orient="records"),
    }