from datetime import datetime

from sqlalchemy.orm import Session

from app.agents.bootstrap import build_default_registry
from app.agents.context import RuntimeContext
from app.agents.runtime import AgentRuntime
from app.agents.types import AgentRole
from app.db.models.task import TaskStatus
from app.schemas.collaboration import CollaborationRunRequest, CollaborationRunResponse, CollaborationSessionsResponse
from app.schemas.task import TaskCreateRequest, TaskUpdateStatusRequest
from app.services.memory_service import MemoryService
from app.services.realtime_service import emit_event
from app.services.task_service import TaskService
from app.services.tool_service import ToolService


class CollaborationService:
    _session_store: list[dict] = []

    def __init__(self, db: Session):
        self.task_service = TaskService(db)
        self.memory_service = MemoryService(db)
        self.tool_service = ToolService()
        self.runtime = AgentRuntime(build_default_registry())

    def run(self, payload: CollaborationRunRequest) -> CollaborationRunResponse:
        if payload.task_id:
            task = self.task_service.get_task(payload.task_id)
            if not task:
                raise ValueError('Task not found')
        else:
            title = payload.title or payload.objective[:80]
            task = self.task_service.create_task(TaskCreateRequest(title=title, prompt=payload.objective))

        emit_event('collaboration', 'Collaboration run started', {'task_id': task.id, 'rounds': payload.rounds})

        context = RuntimeContext(task_id=task.id, objective=payload.objective)

        def tool_executor(name: str, data: dict):
            result = self.tool_service.execute_tool(name, data)
            context.add_timeline_event('tool_execution', f'Tool executed: {name}', {'status': result.status})
            emit_event('tool_execution', f'Tool executed: {name}', {'status': result.status, 'task_id': task.id})
            return result

        context.set_state('tool_executor', tool_executor)

        started_at = datetime.utcnow()

        def on_step(role: AgentRole, run_context: RuntimeContext, round_index: int):
            stage = f'collab_round_{round_index}'
            self.task_service.update_status(
                task.id,
                TaskUpdateStatusRequest(status=TaskStatus.executing, result=None, error=None),
            )
            run_context.add_timeline_event(stage, f'{role.value} engaged in collaborative turn', {'round': round_index})
            emit_event(stage, f'{role.value} engaged in collaborative turn', {'task_id': task.id, 'round': round_index})

        session, transcript = self.runtime.run_collaborative(context=context, rounds=payload.rounds, on_step=on_step)

        final_summary = f'Collaborative run completed across {payload.rounds} rounds.'
        final_task = self.task_service.update_status(
            task.id,
            TaskUpdateStatusRequest(status=TaskStatus.completed, result=final_summary, error=None),
        )
        if not final_task:
            raise ValueError('Failed to update final task state')

        emit_event('completed', 'Collaboration session completed', {'task_id': task.id, 'session_id': session.get('session_id')})

        completed_at = datetime.utcnow()
        CollaborationService._session_store.append(session)

        return CollaborationRunResponse(
            task_id=task.id,
            objective=payload.objective,
            rounds=payload.rounds,
            session=session,
            transcript=transcript.as_dict(timeline=context.timeline_events),
            timeline=context.timeline_events,
            started_at=started_at,
            completed_at=completed_at,
        )

    def sessions(self) -> CollaborationSessionsResponse:
        items = CollaborationService._session_store[-20:]
        return CollaborationSessionsResponse(items=items, count=len(items))
