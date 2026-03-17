from dataclasses import dataclass, field
from datetime import datetime

from app.agents.contracts import AgentMessage
from app.agents.types import AgentRole


@dataclass
class CollaborationMessageBus:
    queue: list[AgentMessage] = field(default_factory=list)
    delivered: list[AgentMessage] = field(default_factory=list)

    def publish(self, message: AgentMessage) -> None:
        self.queue.append(message)

    def publish_many(self, messages: list[AgentMessage]) -> None:
        for message in messages:
            self.publish(message)

    def drain_for(self, role: AgentRole) -> list[AgentMessage]:
        matched = [message for message in self.queue if message.to_agent == role]
        self.queue = [message for message in self.queue if message.to_agent != role]
        self.delivered.extend(matched)
        return matched

    def all_messages(self) -> list[AgentMessage]:
        return self.delivered + self.queue


@dataclass
class CollaborationEvent:
    stage: str
    message: str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    metadata: dict = field(default_factory=dict)
