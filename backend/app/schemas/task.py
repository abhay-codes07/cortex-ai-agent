from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.db.models.task import TaskStatus


class TaskCreateRequest(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    prompt: str = Field(min_length=5, max_length=5000)


class TaskUpdateStatusRequest(BaseModel):
    status: TaskStatus
    result: Optional[str] = Field(default=None, max_length=20000)
    error: Optional[str] = Field(default=None, max_length=5000)


class TaskResponse(BaseModel):
    id: str
    title: str
    prompt: str
    status: TaskStatus
    result: Optional[str]
    error: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TaskListResponse(BaseModel):
    items: list[TaskResponse]
    count: int


class TaskSummaryResponse(BaseModel):
    total: int
    queued: int
    in_progress: int
    completed: int
    failed: int
