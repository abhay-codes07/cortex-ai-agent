from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class MemoryCreateRequest(BaseModel):
    task_id: str = Field(min_length=3, max_length=128)
    objective: str = Field(min_length=5, max_length=5000)
    summary: str = Field(min_length=5, max_length=20000)
    workflow_mode: str = Field(min_length=3, max_length=120)
    strategy: Optional[str] = Field(default=None, max_length=200)
    plan_steps: list[str] = Field(default_factory=list)
    deliverables: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)


class MemoryRecallRequest(BaseModel):
    objective: str = Field(min_length=5, max_length=5000)
    limit: int = Field(default=5, ge=1, le=20)


class MemoryRecordResponse(BaseModel):
    id: str
    task_id: str
    objective: str
    summary: str
    workflow_mode: str
    strategy: Optional[str]
    plan_steps: list[str]
    deliverables: list[str]
    tags: list[str]
    relevance_score: Optional[float] = None
    created_at: datetime


class MemoryListResponse(BaseModel):
    items: list[MemoryRecordResponse]
    count: int


class MemoryRecallResponse(BaseModel):
    objective: str
    items: list[MemoryRecordResponse]
    count: int
