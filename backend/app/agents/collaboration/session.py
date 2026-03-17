from dataclasses import dataclass, field
from datetime import datetime

from app.agents.collaboration.message_bus import CollaborationEvent
from app.agents.contracts import AgentResult


@dataclass
class CollaborationSession:
    session_id: str
    task_id: str
    objective: str
    rounds: int
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    events: list[CollaborationEvent] = field(default_factory=list)
    results: list[AgentResult] = field(default_factory=list)

    def add_event(self, stage: str, message: str, metadata: dict | None = None) -> None:
        self.events.append(CollaborationEvent(stage=stage, message=message, metadata=metadata or {}))

    def add_result(self, result: AgentResult) -> None:
        self.results.append(result)

    def to_dict(self) -> dict:
        return {
            'session_id': self.session_id,
            'task_id': self.task_id,
            'objective': self.objective,
            'rounds': self.rounds,
            'created_at': self.created_at,
            'events': [
                {
                    'stage': event.stage,
                    'message': event.message,
                    'timestamp': event.timestamp,
                    'metadata': event.metadata,
                }
                for event in self.events
            ],
            'results': [result.model_dump(mode='json') for result in self.results],
        }
