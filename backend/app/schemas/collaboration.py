from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class CollaborationRunRequest(BaseModel):
    task_id: str | None = None
    title: str | None = Field(default=None, min_length=3, max_length=200)
    objective: str = Field(min_length=5, max_length=5000)
    rounds: int = Field(default=2, ge=1, le=5)


class CollaborationRunResponse(BaseModel):
    task_id: str
    objective: str
    rounds: int
    session: dict[str, Any]
    transcript: dict[str, Any]
    timeline: list[dict[str, Any]]
    started_at: datetime
    completed_at: datetime


class CollaborationSessionsResponse(BaseModel):
    items: list[dict[str, Any]]
    count: int
