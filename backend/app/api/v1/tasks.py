from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db_session
from app.schemas.task import (
    TaskCreateRequest,
    TaskListResponse,
    TaskResponse,
    TaskSummaryResponse,
    TaskUpdateStatusRequest,
)
from app.services.task_service import TaskService

router = APIRouter()


def get_task_service(db: Session = Depends(get_db_session)) -> TaskService:
    return TaskService(db)


@router.post('/tasks', response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreateRequest, service: TaskService = Depends(get_task_service)) -> TaskResponse:
    return service.create_task(payload)


@router.get('/tasks', response_model=TaskListResponse)
def list_tasks(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    service: TaskService = Depends(get_task_service),
) -> TaskListResponse:
    return service.list_tasks(limit=limit, offset=offset)


@router.get('/tasks/summary', response_model=TaskSummaryResponse)
def summarize_tasks(service: TaskService = Depends(get_task_service)) -> TaskSummaryResponse:
    return service.summarize()


@router.get('/tasks/{task_id}', response_model=TaskResponse)
def get_task(task_id: str, service: TaskService = Depends(get_task_service)) -> TaskResponse:
    task = service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    return task


@router.patch('/tasks/{task_id}/status', response_model=TaskResponse)
def update_task_status(
    task_id: str,
    payload: TaskUpdateStatusRequest,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    task = service.update_status(task_id, payload)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    return task


@router.post('/tasks/{task_id}/start', response_model=TaskResponse)
def start_task(task_id: str, service: TaskService = Depends(get_task_service)) -> TaskResponse:
    task = service.mark_started(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    return task
