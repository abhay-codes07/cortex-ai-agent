from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class ToolCall(BaseModel):
    name: str
    payload: dict[str, Any] = Field(default_factory=dict)


class ToolResult(BaseModel):
    tool: str
    status: str
    output: dict[str, Any] = Field(default_factory=dict)
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())


class BaseTool(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, payload: dict[str, Any]) -> ToolResult:
        raise NotImplementedError
