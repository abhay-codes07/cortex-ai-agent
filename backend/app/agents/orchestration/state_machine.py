from dataclasses import dataclass

from app.agents.types import AgentRole
from app.db.models.task import TaskStatus


@dataclass
class WorkflowState:
    name: str
    task_status: TaskStatus


class OrchestrationStateMachine:
    def __init__(self) -> None:
        self.states = [
            WorkflowState(name='orchestrating', task_status=TaskStatus.planning),
            WorkflowState(name='planning', task_status=TaskStatus.planning),
            WorkflowState(name='researching', task_status=TaskStatus.researching),
            WorkflowState(name='deciding', task_status=TaskStatus.deciding),
            WorkflowState(name='executing', task_status=TaskStatus.executing),
            WorkflowState(name='memory_sync', task_status=TaskStatus.executing),
            WorkflowState(name='completed', task_status=TaskStatus.completed),
        ]
        self.role_stage_map = {
            AgentRole.orchestrator: 'orchestrating',
            AgentRole.planner: 'planning',
            AgentRole.research: 'researching',
            AgentRole.decision: 'deciding',
            AgentRole.execution: 'executing',
            AgentRole.memory: 'memory_sync',
        }

    def sequence(self) -> list[WorkflowState]:
        return self.states

    def status_for(self, state_name: str) -> TaskStatus:
        for state in self.states:
            if state.name == state_name:
                return state.task_status
        return TaskStatus.executing

    def stage_for_role(self, role: AgentRole) -> str:
        return self.role_stage_map.get(role, 'executing')
