from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class RuntimeContext:
    task_id: str
    objective: str
    short_term_memory: dict[str, Any] = field(default_factory=dict)
    shared_state: dict[str, Any] = field(default_factory=dict)
    started_at: datetime = field(default_factory=datetime.utcnow)

    def remember(self, key: str, value: Any) -> None:
        self.short_term_memory[key] = value

    def recall(self, key: str, default: Any = None) -> Any:
        return self.short_term_memory.get(key, default)

    def set_state(self, key: str, value: Any) -> None:
        self.shared_state[key] = value

    def get_state(self, key: str, default: Any = None) -> Any:
        return self.shared_state.get(key, default)
