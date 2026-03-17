from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class RuntimeContext:
    task_id: str
    objective: str
    short_term_memory: dict[str, Any] = field(default_factory=dict)
    shared_state: dict[str, Any] = field(default_factory=dict)
    timeline_events: list[dict[str, Any]] = field(default_factory=list)
    started_at: datetime = field(default_factory=datetime.utcnow)

    def remember(self, key: str, value: Any) -> None:
        self.short_term_memory[key] = value

    def recall(self, key: str, default: Any = None) -> Any:
        return self.short_term_memory.get(key, default)

    def set_state(self, key: str, value: Any) -> None:
        self.shared_state[key] = value

    def get_state(self, key: str, default: Any = None) -> Any:
        return self.shared_state.get(key, default)

    def read_inbox(self, role_name: str) -> list[dict[str, Any]]:
        return self.get_state(f'inbox:{role_name}', [])

    def add_timeline_event(self, stage: str, message: str, metadata: dict[str, Any] | None = None) -> None:
        self.timeline_events.append(
            {
                'stage': stage,
                'message': message,
                'metadata': metadata or {},
                'timestamp': datetime.utcnow().isoformat(),
            }
        )
