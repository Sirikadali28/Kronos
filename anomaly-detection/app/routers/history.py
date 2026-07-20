from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.permissions import require_roles
from app.db.user import User
from app.repositories.detection_repository import DetectionRepository
from app.schemas.history import HistoryListResponse, HistoryResponse

router = APIRouter(
    prefix="/history",
    tags=["History"],
)


@router.get("/", response_model=HistoryListResponse)
async def get_history(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(
        require_roles(
            "admin",
            "analyst",
            "viewer",
        ),
    ),
):
    """
    Retrieve paginated detection history.
    """

    repository = DetectionRepository(db)

    total = await repository.count()
    items = await repository.get_paginated(skip, limit)

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "items": items,
    }


@router.get("/{history_id}", response_model=HistoryResponse)
async def get_history_by_id(
    history_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(
        require_roles(
            "admin",
            "analyst",
            "viewer",
        ),
    ),
):
    """
    Retrieve a detection history record by ID.
    """

    repository = DetectionRepository(db)

    history = await repository.get_by_id(history_id)

    if history is None:
        raise HTTPException(
            status_code=404,
            detail="History record not found.",
        )

    return history
