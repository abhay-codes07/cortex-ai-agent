from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from app.agents.types import AgentRole


class AgentMessage(BaseModel):
    from_agent: AgentRole
    to_agent: AgentRole
    content: str = Field(min_length=1, max_length=3000)
    metadata: dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AgentThought(BaseModel):
    agent: AgentRole
    step: str = Field(min_length=1, max_length=300)
    reasoning: str = Field(min_length=1, max_length=3000)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AgentAction(BaseModel):
    agent: AgentRole
    action: str = Field(min_length=1, max_length=150)
    payload: dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AgentResult(BaseModel):
    agent: AgentRole
    status: str
    output: dict[str, Any] = Field(default_factory=dict)
    thoughts: list[AgentThought] = Field(default_factory=list)
    actions: list[AgentAction] = Field(default_factory=list)
    messages: list[AgentMessage] = Field(default_factory=list)
