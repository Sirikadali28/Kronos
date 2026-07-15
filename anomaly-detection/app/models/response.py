from typing import Any

from pydantic import BaseModel, ConfigDict


class APIResponse(BaseModel):
    """
    Standard API response model.
    """
    model_config = ConfigDict(from_attributes=True)

    status: str
    message: str
    data: Any | None = None


class ErrorResponse(BaseModel):
    """
    Standard error response model.
    """
    model_config = ConfigDict(from_attributes=True)

    status: str = "error"
    message: str
    detail: Any | None = None

    status: str = "error"
    message: str