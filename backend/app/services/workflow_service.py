from datetime import datetime

from sqlalchemy.orm import Session

from app.agents.bootstrap import build_default_registry
from app.agents.orchestration import OrchestrationCoordinator, WorkflowEventLogger
from app.agents.runtime import AgentRuntime
from app.agents.types import AgentRole
from app.db.models.task import TaskStatus
from app.schemas.memory import MemoryCreateRequest, MemoryRecallRequest
from app.schemas.task import TaskCreateRequest, TaskUpdateStatusRequest
from app.schemas.workflow import WorkflowRunRequest, WorkflowRunResponse
from app.services.memory_service import MemoryService
from app.services.realtime_service import emit_event
from app.services.task_service import TaskService
from app.services.tool_service import ToolService


class WorkflowService:
    def __init__(self, db: Session):
        self.task_service = TaskService(db)
        self.memory_service = MemoryService(db)
        self.tool_service = ToolService()
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

        emit_event('workflow', 'Workflow run started', {'task_id': task.id})

        logger = WorkflowEventLogger()
        context = self.coordinator.prepare_context(task_id=task.id, objective=payload.objective)

        def tool_executor(name: str, data: dict):
            result = self.tool_service.execute_tool(name, data)
            context.add_timeline_event('tool_execution', f"Tool executed: {name}", {'status': result.status})
            logger.add('tool_execution', f"Tool executed: {name}", {'status': result.status})
            emit_event('tool_execution', f'Tool executed: {name}', {'status': result.status, 'task_id': task.id})
            return result

        context.set_state('tool_executor', tool_executor)

        recalled_memory = self.memory_service.recall(MemoryRecallRequest(objective=payload.objective, limit=3))
        hints = [item.summary for item in recalled_memory.items[:2]]
        context.remember('memory_hints', hints)
        if hints:
            context.add_timeline_event('memory_recall', 'Loaded relevant long-term memory hints', {'count': len(hints)})
            logger.add('memory_recall', 'Memory recall loaded before orchestration', {'count': len(hints)})
            emit_event('memory_recall', 'Loaded long-term memory hints', {'count': len(hints), 'task_id': task.id})

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
            emit_event(stage, f'{role.value} agent started', {'task_id': task.id})

        transcript = self.runtime.run_once(context, on_step=on_step)

        tool_results = context.get_state('tool_results', [])
        final_summary = (
            'Workflow executed successfully with orchestrator-planner intelligence and tool execution enabled. '
            f"Tool calls: {len(tool_results)}."
        )
        final_task = self.task_service.update_status(
            task.id,
            TaskUpdateStatusRequest(status=TaskStatus.completed, result=final_summary, error=None),
        )
        if not final_task:
            raise ValueError('Failed to persist final task state')

        logger.add('completed', 'Workflow completed successfully', {'task_id': task.id})
        context.add_timeline_event('completed', 'Workflow completed successfully')
        emit_event('completed', 'Workflow completed successfully', {'task_id': task.id})

        memory_snapshot = context.recall('memory_snapshot', {})
        strategy = context.get_state('selected_strategy', {}).get('strategy')
        plan_steps = memory_snapshot.get('plan_steps', context.recall('plan_steps', []))
        deliverables = memory_snapshot.get('deliverables', context.get_state('deliverables', []))

        memory_summary = (
            f"Workflow mode {memory_snapshot.get('workflow_mode', 'iterative-safe')} with {len(plan_steps)} plan steps and "
            f"{len(deliverables)} deliverables."
        )
        memory_tags = ['workflow', memory_snapshot.get('workflow_mode', 'iterative-safe'), strategy or 'unknown', 'tools']

        self.memory_service.create_record(
            MemoryCreateRequest(
                task_id=task.id,
                objective=payload.objective,
                summary=memory_summary,
                workflow_mode=memory_snapshot.get('workflow_mode', 'iterative-safe'),
                strategy=strategy,
                plan_steps=plan_steps,
                deliverables=deliverables,
                tags=memory_tags,
            )
        )
        context.add_timeline_event('memory_persist', 'Stored long-term memory record from workflow output')
        logger.add('memory_persist', 'Long-term memory record stored', {'task_id': task.id})
        emit_event('memory_persist', 'Long-term memory record stored', {'task_id': task.id})

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
