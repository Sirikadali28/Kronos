from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class HistoryResponse(BaseModel):
    id: UUID
    created_at: datetime
    records_processed: int
    anomaly_count: int
    status: str
    execution_time_ms: float
    algorithm_version: str
    report_path: str | None

    model_config = {"from_attributes": True}


class HistoryListResponse(BaseModel):
    total: int
    skip: int
    limit: int
    items: list[HistoryResponse]
