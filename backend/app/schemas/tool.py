from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class ToolDescriptor(BaseModel):
    name: str
    description: str


class ToolExecuteRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    payload: dict[str, Any] = Field(default_factory=dict)


class ToolExecuteResponse(BaseModel):
    tool: str
    status: str
    output: dict[str, Any]
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())


class ToolBatchExecuteRequest(BaseModel):
    calls: list[ToolExecuteRequest] = Field(default_factory=list)


class ToolBatchExecuteResponse(BaseModel):
    results: list[ToolExecuteResponse]
    count: int
