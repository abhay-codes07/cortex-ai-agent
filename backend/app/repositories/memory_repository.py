import json
from collections import Counter

from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.db.models.memory_record import MemoryRecord


class MemoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        task_id: str,
        objective: str,
        summary: str,
        workflow_mode: str,
        strategy: str | None,
        plan_steps: list[str],
        deliverables: list[str],
        tags: list[str],
    ) -> MemoryRecord:
        record = MemoryRecord(
            task_id=task_id,
            objective=objective,
            summary=summary,
            workflow_mode=workflow_mode,
            strategy=strategy,
            plan_steps=json.dumps(plan_steps),
            deliverables=json.dumps(deliverables),
            tags=json.dumps(tags),
        )
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record

    def list_recent(self, limit: int = 20, offset: int = 0) -> list[MemoryRecord]:
        stmt = select(MemoryRecord).order_by(desc(MemoryRecord.created_at)).offset(offset).limit(limit)
        return list(self.db.execute(stmt).scalars().all())

    def recall(self, objective: str, limit: int = 5) -> list[tuple[MemoryRecord, float]]:
        objective_terms = self._terms(objective)
        records = self.list_recent(limit=250, offset=0)

        scored: list[tuple[MemoryRecord, float]] = []
        for record in records:
            record_terms = self._terms(
                f"{record.objective} {record.summary} {record.workflow_mode} {record.strategy or ''} {record.tags}"
            )
            score = self._overlap_score(objective_terms, record_terms)
            if score > 0:
                scored.append((record, score))

        scored.sort(key=lambda item: item[1], reverse=True)
        return scored[:limit]

    def _terms(self, text: str) -> Counter:
        tokens = [token.strip('.,:;!?()[]{}"\'').lower() for token in text.split()]
        filtered = [token for token in tokens if len(token) > 2]
        return Counter(filtered)

    def _overlap_score(self, left: Counter, right: Counter) -> float:
        if not left or not right:
            return 0.0
        common = set(left.keys()) & set(right.keys())
        if not common:
            return 0.0
        numerator = sum(min(left[token], right[token]) for token in common)
        denominator = max(sum(left.values()), 1)
        return numerator / denominator
