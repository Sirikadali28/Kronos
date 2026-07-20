from pydantic import BaseModel, Field


class DetectionRequest(BaseModel):
    """
    Request model for anomaly detection.
    """

    values: list[float] = Field(
        ...,
        min_length=10,
        description="Time-series values to analyze.",
    )

    column_name: str = Field(
        default="value",
        description="Column containing the values.",
    )
