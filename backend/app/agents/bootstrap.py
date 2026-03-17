from app.agents.implementations.decision import DecisionAgent
from app.agents.implementations.execution import ExecutionAgent
from app.agents.implementations.memory import MemoryAgent
from app.agents.implementations.orchestrator import OrchestratorAgent
from app.agents.implementations.planner import PlannerAgent
from app.agents.implementations.research import ResearchAgent
from app.agents.registry import AgentRegistry


def build_default_registry() -> AgentRegistry:
    registry = AgentRegistry()
    registry.register(OrchestratorAgent())
    registry.register(PlannerAgent())
    registry.register(ResearchAgent())
    registry.register(DecisionAgent())
    registry.register(ExecutionAgent())
    registry.register(MemoryAgent())
    return registry
