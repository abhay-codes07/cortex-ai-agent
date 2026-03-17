from app.agents.base import BaseAgent
from app.agents.types import AgentRole


class AgentRegistry:
    def __init__(self) -> None:
        self._agents: dict[AgentRole, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        self._agents[agent.role] = agent

    def get(self, role: AgentRole) -> BaseAgent | None:
        return self._agents.get(role)

    def require(self, role: AgentRole) -> BaseAgent:
        agent = self.get(role)
        if not agent:
            raise ValueError(f'Agent not registered: {role.value}')
        return agent

    def list_roles(self) -> list[AgentRole]:
        return list(self._agents.keys())

    def list_names(self) -> list[str]:
        return [agent.name for agent in self._agents.values()]
