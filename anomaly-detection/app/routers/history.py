from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.repositories.detection_repository import DetectionRepository

router = APIRouter(
    prefix="/history",
    tags=["History"],
)


@router.get("/")
async def get_history(
    db: AsyncSession = Depends(get_db),
):
    """
    Return all detection history records.
    """

    repository = DetectionRepository(db)

    history = await repository.get_all()

    return {
        "count": len(history),
        "history": history,
    }