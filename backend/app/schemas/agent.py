from datetime import datetime

from pydantic import BaseModel, Field


class AgentSimulationRequest(BaseModel):
    task_id: str = Field(min_length=3, max_length=128)
    objective: str = Field(min_length=5, max_length=5000)


class AgentNodeStatus(BaseModel):
    role: str
    name: str
    status: str


class AgentSimulationResponse(BaseModel):
    task_id: str
    objective: str
    started_at: datetime
    completed_at: datetime
    nodes: list[AgentNodeStatus]
    transcript: dict
