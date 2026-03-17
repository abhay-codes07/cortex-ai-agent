from datetime import datetime
import uuid
from typing import Any

from pydantic import BaseModel, Field


class RealtimeEvent(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str = 'event'
    stage: str
    message: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())


class RealtimeStatus(BaseModel):
    connections: int
    channels: list[str] = Field(default_factory=lambda: ['workflow', 'collaboration', 'tools', 'system'])
