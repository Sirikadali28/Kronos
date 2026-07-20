from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.job_history import JobHistory


class JobRepository:
    """
    Repository for background jobs.
    """

    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, job: JobHistory) -> JobHistory:
        self.db.add(job)
        await self.db.commit()
        await self.db.refresh(job)
        return job

    async def update(self, job: JobHistory) -> JobHistory:
        await self.db.commit()
        await self.db.refresh(job)
        return job

    async def get_by_task_id(
        self,
        task_id: str,
    ) -> JobHistory | None:
        result = await self.db.execute(
            select(JobHistory).where(JobHistory.celery_task_id == task_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self):
        result = await self.db.execute(
            select(JobHistory).order_by(JobHistory.created_at.desc())
        )
        return list(result.scalars().all())
