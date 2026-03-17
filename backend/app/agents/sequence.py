from app.agents.types import AgentRole

DEFAULT_AGENT_SEQUENCE = [
    AgentRole.orchestrator,
    AgentRole.planner,
    AgentRole.research,
    AgentRole.decision,
    AgentRole.execution,
    AgentRole.memory,
]
