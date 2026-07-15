from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy ORM models.
    """
    pass


engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
    future=True,
)

SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    """
    FastAPI dependency that provides
    a database session.
    """

    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()