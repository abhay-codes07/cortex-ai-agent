from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.db.models.task import Task, TaskStatus


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, title: str, prompt: str) -> Task:
        task = Task(title=title, prompt=prompt, status=TaskStatus.queued)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get(self, task_id: str) -> Task | None:
        stmt = select(Task).where(Task.id == task_id)
        return self.db.execute(stmt).scalar_one_or_none()

    def list_recent(self, limit: int = 20, offset: int = 0) -> list[Task]:
        stmt = select(Task).order_by(desc(Task.created_at)).offset(offset).limit(limit)
        return list(self.db.execute(stmt).scalars().all())

    def update_status(self, task: Task, status: TaskStatus, result: str | None, error: str | None) -> Task:
        task.status = status
        if result is not None:
            task.result = result
        if error is not None:
            task.error = error

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def summary_counts(self) -> dict[str, int]:
        tasks = self.list_recent(limit=1000, offset=0)
        total = len(tasks)
        queued = sum(1 for task in tasks if task.status == TaskStatus.queued)
        completed = sum(1 for task in tasks if task.status == TaskStatus.completed)
        failed = sum(1 for task in tasks if task.status == TaskStatus.failed)
        in_progress = total - queued - completed - failed

        return {
            'total': total,
            'queued': queued,
            'in_progress': in_progress,
            'completed': completed,
            'failed': failed,
        }
