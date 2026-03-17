from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models.task import TaskStatus
from app.repositories.task_repository import TaskRepository
from app.schemas.task import (
    TaskCreateRequest,
    TaskListResponse,
    TaskResponse,
    TaskSummaryResponse,
    TaskUpdateStatusRequest,
)
from app.services.cache_service import CacheService
from app.services.realtime_service import emit_event


class TaskService:
    def __init__(self, db: Session, cache: CacheService | None = None):
        self.repository = TaskRepository(db)
        self.cache = cache or CacheService()

    def create_task(self, payload: TaskCreateRequest) -> TaskResponse:
        task = self.repository.create(title=payload.title, prompt=payload.prompt)
        response = TaskResponse.model_validate(task)

        self.cache.set_json(f'task:{task.id}', response.model_dump(mode='json'))
        self.cache.invalidate('task:list')
        self.cache.invalidate('task:summary')
        emit_event('task_created', f'Task created: {task.title}', {'task_id': task.id})

        return response

    def get_task(self, task_id: str) -> TaskResponse | None:
        cached = self.cache.get_json(f'task:{task_id}')
        if cached:
            return TaskResponse.model_validate(cached)

        task = self.repository.get(task_id)
        if not task:
            return None

        response = TaskResponse.model_validate(task)
        self.cache.set_json(f'task:{task.id}', response.model_dump(mode='json'))
        return response

    def list_tasks(self, limit: int = 20, offset: int = 0) -> TaskListResponse:
        if limit == 20 and offset == 0:
            cached = self.cache.get_json('task:list')
            if cached:
                return TaskListResponse.model_validate(cached)

        items = [TaskResponse.model_validate(task) for task in self.repository.list_recent(limit, offset)]
        payload = TaskListResponse(items=items, count=len(items))

        if limit == 20 and offset == 0:
            self.cache.set_json('task:list', payload.model_dump(mode='json'))
        return payload

    def update_status(self, task_id: str, payload: TaskUpdateStatusRequest) -> TaskResponse | None:
        task = self.repository.get(task_id)
        if not task:
            return None

        task = self.repository.update_status(
            task=task,
            status=payload.status,
            result=payload.result,
            error=payload.error,
        )

        response = TaskResponse.model_validate(task)
        self.cache.set_json(f'task:{task.id}', response.model_dump(mode='json'))
        self.cache.invalidate('task:list')
        self.cache.invalidate('task:summary')
        emit_event('task_status', f'Task status updated: {payload.status.value}', {'task_id': task.id, 'status': payload.status.value})

        return response

    def summarize(self) -> TaskSummaryResponse:
        cached = self.cache.get_json('task:summary')
        if cached:
            return TaskSummaryResponse.model_validate(cached)

        counts = self.repository.summary_counts()
        response = TaskSummaryResponse(**counts)
        self.cache.set_json('task:summary', response.model_dump(mode='json'), ttl=settings.redis_ttl_seconds)
        return response

    def mark_started(self, task_id: str) -> TaskResponse | None:
        return self.update_status(
            task_id,
            TaskUpdateStatusRequest(status=TaskStatus.executing, result=None, error=None),
        )
