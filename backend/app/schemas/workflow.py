from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.task import TaskResponse


class WorkflowRunRequest(BaseModel):
    task_id: str | None = None
    title: str | None = Field(default=None, min_length=3, max_length=200)
    objective: str = Field(min_length=5, max_length=5000)


class WorkflowRunResponse(BaseModel):
    task: TaskResponse
    mode: str
    started_at: datetime
    completed_at: datetime
    timeline: list[dict]
    transcript: dict
    plan_overview: list[str]
