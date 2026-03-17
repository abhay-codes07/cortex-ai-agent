from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db_session
from app.schemas.memory import (
    MemoryCreateRequest,
    MemoryListResponse,
    MemoryRecallRequest,
    MemoryRecallResponse,
    MemoryRecordResponse,
)
from app.services.memory_service import MemoryService

router = APIRouter(prefix='/memory')


def get_memory_service(db: Session = Depends(get_db_session)) -> MemoryService:
    return MemoryService(db)


@router.post('/records', response_model=MemoryRecordResponse, status_code=status.HTTP_201_CREATED)
def create_record(
    payload: MemoryCreateRequest,
    service: MemoryService = Depends(get_memory_service),
) -> MemoryRecordResponse:
    return service.create_record(payload)


@router.get('/recent', response_model=MemoryListResponse)
def recent_records(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    service: MemoryService = Depends(get_memory_service),
) -> MemoryListResponse:
    return service.list_recent(limit=limit, offset=offset)


@router.post('/recall', response_model=MemoryRecallResponse)
def recall_records(
    payload: MemoryRecallRequest,
    service: MemoryService = Depends(get_memory_service),
) -> MemoryRecallResponse:
    return service.recall(payload)
