from datetime import datetime

from app.agents.bootstrap import build_default_registry
from app.agents.context import RuntimeContext
from app.agents.runtime import AgentRuntime
from app.schemas.agent import AgentNodeStatus, AgentSimulationRequest, AgentSimulationResponse


class AgentSystemService:
    def __init__(self) -> None:
        self.registry = build_default_registry()
        self.runtime = AgentRuntime(self.registry)

    def list_nodes(self) -> list[AgentNodeStatus]:
        nodes: list[AgentNodeStatus] = []
        for role in self.registry.list_roles():
            agent = self.registry.require(role)
            nodes.append(AgentNodeStatus(role=role.value, name=agent.name, status='ready'))
        return nodes

    def simulate(self, payload: AgentSimulationRequest) -> AgentSimulationResponse:
        context = RuntimeContext(task_id=payload.task_id, objective=payload.objective)
        started_at = datetime.utcnow()
        transcript = self.runtime.run_once(context)
        completed_at = datetime.utcnow()

        return AgentSimulationResponse(
            task_id=payload.task_id,
            objective=payload.objective,
            started_at=started_at,
            completed_at=completed_at,
            nodes=self.list_nodes(),
            transcript=transcript.as_dict(timeline=context.timeline_events),
        )
