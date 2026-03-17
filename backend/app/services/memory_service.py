import hashlib
import json

from sqlalchemy.orm import Session

from app.core.config import settings
from app.repositories.memory_repository import MemoryRepository
from app.schemas.memory import (
    MemoryCreateRequest,
    MemoryListResponse,
    MemoryRecallRequest,
    MemoryRecallResponse,
    MemoryRecordResponse,
)
from app.services.cache_service import CacheService


class MemoryService:
    def __init__(self, db: Session, cache: CacheService | None = None):
        self.repository = MemoryRepository(db)
        self.cache = cache or CacheService()

    def create_record(self, payload: MemoryCreateRequest) -> MemoryRecordResponse:
        record = self.repository.create(
            task_id=payload.task_id,
            objective=payload.objective,
            summary=payload.summary,
            workflow_mode=payload.workflow_mode,
            strategy=payload.strategy,
            plan_steps=payload.plan_steps,
            deliverables=payload.deliverables,
            tags=payload.tags,
        )
        response = self._to_response(record)
        self.cache.invalidate('memory:recent')
        self.cache.set_json(f'memory:{response.id}', response.model_dump(mode='json'))
        return response

    def list_recent(self, limit: int = 20, offset: int = 0) -> MemoryListResponse:
        if limit == 20 and offset == 0:
            cached = self.cache.get_json('memory:recent')
            if cached:
                return MemoryListResponse.model_validate(cached)

        records = self.repository.list_recent(limit=limit, offset=offset)
        items = [self._to_response(record) for record in records]
        response = MemoryListResponse(items=items, count=len(items))

        if limit == 20 and offset == 0:
            self.cache.set_json('memory:recent', response.model_dump(mode='json'))
        return response

    def recall(self, payload: MemoryRecallRequest) -> MemoryRecallResponse:
        limit = payload.limit or settings.memory_recall_default_limit
        cache_key = self._recall_cache_key(payload.objective, limit)

        cached = self.cache.get_json(cache_key)
        if cached:
            return MemoryRecallResponse.model_validate(cached)

        scored = self.repository.recall(payload.objective, limit=limit)
        items = [self._to_response(record, relevance_score=score) for record, score in scored]
        response = MemoryRecallResponse(objective=payload.objective, items=items, count=len(items))

        self.cache.set_json(cache_key, response.model_dump(mode='json'), ttl=settings.memory_recall_cache_ttl)
        return response

    def _to_response(self, record, relevance_score: float | None = None) -> MemoryRecordResponse:
        return MemoryRecordResponse(
            id=record.id,
            task_id=record.task_id,
            objective=record.objective,
            summary=record.summary,
            workflow_mode=record.workflow_mode,
            strategy=record.strategy,
            plan_steps=self._safe_load_list(record.plan_steps),
            deliverables=self._safe_load_list(record.deliverables),
            tags=self._safe_load_list(record.tags),
            relevance_score=relevance_score,
            created_at=record.created_at,
        )

    def _safe_load_list(self, serialized: str) -> list[str]:
        try:
            data = json.loads(serialized)
        except json.JSONDecodeError:
            return []
        if isinstance(data, list):
            return [str(item) for item in data]
        return []

    def _recall_cache_key(self, objective: str, limit: int) -> str:
        digest = hashlib.sha1(objective.encode('utf-8')).hexdigest()
        return f'memory:recall:{digest}:{limit}'
