from datetime import datetime

from sqlalchemy.orm import Session

from app.agents.bootstrap import build_default_registry
from app.agents.orchestration import OrchestrationCoordinator, WorkflowEventLogger
from app.agents.runtime import AgentRuntime
from app.agents.types import AgentRole
from app.db.models.task import TaskStatus
from app.schemas.task import TaskCreateRequest, TaskUpdateStatusRequest
from app.schemas.workflow import WorkflowRunRequest, WorkflowRunResponse
from app.services.task_service import TaskService


class WorkflowService:
    def __init__(self, db: Session):
        self.task_service = TaskService(db)
        self.registry = build_default_registry()
        self.runtime = AgentRuntime(self.registry)
        self.coordinator = OrchestrationCoordinator()

    def run(self, payload: WorkflowRunRequest) -> WorkflowRunResponse:
        if payload.task_id:
            task = self.task_service.get_task(payload.task_id)
            if not task:
                raise ValueError('Task not found')
        else:
            title = payload.title or payload.objective[:80]
            task = self.task_service.create_task(TaskCreateRequest(title=title, prompt=payload.objective))

        logger = WorkflowEventLogger()
        context = self.coordinator.prepare_context(task_id=task.id, objective=payload.objective)

        started_at = datetime.utcnow()

        def on_step(role: AgentRole, run_context):
            stage = self.coordinator.stage_for_role(role)
            status = self.coordinator.status_for_role(role)
            self.task_service.update_status(
                task.id,
                TaskUpdateStatusRequest(status=status, result=None, error=None),
            )
            logger.add(stage, f'{role.value} agent started', {'task_id': task.id})
            run_context.add_timeline_event(stage, f'{role.value} agent started')

        transcript = self.runtime.run_once(context, on_step=on_step)

        final_summary = 'Workflow executed successfully with orchestrator-planner intelligence enabled.'
        final_task = self.task_service.update_status(
            task.id,
            TaskUpdateStatusRequest(status=TaskStatus.completed, result=final_summary, error=None),
        )
        if not final_task:
            raise ValueError('Failed to persist final task state')

        logger.add('completed', 'Workflow completed successfully', {'task_id': task.id})
        context.add_timeline_event('completed', 'Workflow completed successfully')

        completed_at = datetime.utcnow()

        plan_overview = context.recall('plan_steps', [])
        workflow_mode = context.get_state('workflow_mode', 'iterative-safe')

        combined_timeline = logger.events + context.timeline_events

        return WorkflowRunResponse(
            task=final_task,
            mode=workflow_mode,
            started_at=started_at,
            completed_at=completed_at,
            timeline=combined_timeline,
            transcript=transcript.as_dict(timeline=combined_timeline),
            plan_overview=plan_overview,
        )
