from typing import Any

from pydantic import BaseModel


class APIResponse(BaseModel):
    """
    Standard API response model.
    """

    status: str
    message: str
    data: Any | None = None


class ErrorResponse(BaseModel):
    """
    Standard error response model.
    """

    status: str = "error"
    message: str