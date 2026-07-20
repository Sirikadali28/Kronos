import uuid
from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DetectionHistory(Base):
    """
    Stores the execution history of anomaly detection requests.
    """

    __tablename__ = "detection_history"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True,
    )

    records_processed: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    anomaly_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    execution_time_ms: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    algorithm_version: Mapped[str] = mapped_column(
        String(20),
        default="1.0.0",
        nullable=False,
    )

    report_path: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
