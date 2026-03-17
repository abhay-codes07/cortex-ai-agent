from app.api.v1.agents import router as agents_router
from app.api.v1.health import router as health_router
from app.api.v1.system import router as system_router
from app.api.v1.tasks import router as tasks_router

__all__ = ['agents_router', 'health_router', 'system_router', 'tasks_router']
