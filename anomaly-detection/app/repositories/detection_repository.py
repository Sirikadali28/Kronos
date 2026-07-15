from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.detection_history import DetectionHistory


class DetectionRepository:
    """
    Repository for DetectionHistory operations.
    """

    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, detection: DetectionHistory) -> DetectionHistory:
        self.db.add(detection)
        await self.db.commit()
        await self.db.refresh(detection)
        return detection

    async def get_all(self) -> list[DetectionHistory]:
        result = await self.db.execute(
            select(DetectionHistory).order_by(
                DetectionHistory.created_at.desc()
            )
        )
        return list(result.scalars().all())

    async def get_by_id(
        self,
        detection_id: UUID,
    ) -> DetectionHistory | None:
        result = await self.db.execute(
            select(DetectionHistory).where(
                DetectionHistory.id == detection_id
            )
        )
        return result.scalar_one_or_none()

    async def get_paginated(
        self,
        skip: int = 0,
        limit: int = 10,
    ) -> list[DetectionHistory]:
        result = await self.db.execute(
            select(DetectionHistory)
            .order_by(DetectionHistory.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    async def count(self) -> int:
        result = await self.db.execute(
            select(func.count()).select_from(DetectionHistory)
        )
        return result.scalar_one()