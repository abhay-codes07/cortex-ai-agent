from abc import ABC, abstractmethod

from app.agents.context import RuntimeContext
from app.agents.contracts import AgentAction, AgentMessage, AgentResult, AgentThought
from app.agents.types import AgentRole


class BaseAgent(ABC):
    def __init__(self, role: AgentRole, name: str):
        self.role = role
        self.name = name

    @abstractmethod
    def run(self, context: RuntimeContext) -> AgentResult:
        raise NotImplementedError

    def thought(self, step: str, reasoning: str) -> AgentThought:
        return AgentThought(agent=self.role, step=step, reasoning=reasoning)

    def action(self, action: str, payload: dict | None = None) -> AgentAction:
        return AgentAction(agent=self.role, action=action, payload=payload or {})

    def message(self, to_agent: AgentRole, content: str, metadata: dict | None = None) -> AgentMessage:
        return AgentMessage(
            from_agent=self.role,
            to_agent=to_agent,
            content=content,
            metadata=metadata or {},
        )
