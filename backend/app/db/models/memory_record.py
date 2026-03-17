from datetime import datetime
import uuid

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class MemoryRecord(Base):
    __tablename__ = 'memory_records'

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    task_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    objective: Mapped[str] = mapped_column(Text, nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    workflow_mode: Mapped[str] = mapped_column(String(80), nullable=False)
    strategy: Mapped[str | None] = mapped_column(String(120), nullable=True)

    plan_steps: Mapped[str] = mapped_column(Text, nullable=False)
    deliverables: Mapped[str] = mapped_column(Text, nullable=False)
    tags: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow
    )
