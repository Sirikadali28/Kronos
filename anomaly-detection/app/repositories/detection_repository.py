from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.detection_history import DetectionHistory


class DetectionRepository:
    """
    Repository for DetectionHistory operations.
    """

    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, detection: DetectionHistory) -> DetectionHistory:
        """
        Save a detection history record.
        """
        self.db.add(detection)
        await self.db.commit()
        await self.db.refresh(detection)
        return detection

    async def get_all(self) -> list[DetectionHistory]:
        """
        Retrieve all detection history records.
        """
        result = await self.db.execute(
            select(DetectionHistory).order_by(
                DetectionHistory.created_at.desc()
            )
        )
        return list(result.scalars().all())