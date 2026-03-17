from datetime import datetime

from app.agents.context import RuntimeContext
from app.agents.orchestration.state_machine import OrchestrationStateMachine
from app.agents.types import AgentRole
from app.db.models.task import TaskStatus


class WorkflowEventLogger:
    def __init__(self) -> None:
        self.events: list[dict] = []

    def add(self, stage: str, message: str, metadata: dict | None = None) -> None:
        self.events.append(
            {
                'stage': stage,
                'message': message,
                'metadata': metadata or {},
                'timestamp': datetime.utcnow().isoformat(),
            }
        )


class OrchestrationCoordinator:
    def __init__(self) -> None:
        self.state_machine = OrchestrationStateMachine()

    def prepare_context(self, task_id: str, objective: str) -> RuntimeContext:
        context = RuntimeContext(task_id=task_id, objective=objective)
        context.set_state('workflow_states', [state.name for state in self.state_machine.sequence()])
        return context

    def stage_for_role(self, role: AgentRole) -> str:
        return self.state_machine.stage_for_role(role)

    def status_for_role(self, role: AgentRole) -> TaskStatus:
        stage = self.stage_for_role(role)
        return self.state_machine.status_for(stage)
