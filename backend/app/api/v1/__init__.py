from app.api.v1.agents import router as agents_router
from app.api.v1.collaboration import router as collaboration_router
from app.api.v1.demo import router as demo_router
from app.api.v1.health import router as health_router
from app.api.v1.memory import router as memory_router
from app.api.v1.realtime import router as realtime_router
from app.api.v1.system import router as system_router
from app.api.v1.tasks import router as tasks_router
from app.api.v1.tools import router as tools_router
from app.api.v1.workflows import router as workflows_router

__all__ = [
    'agents_router',
    'collaboration_router',
    'demo_router',
    'health_router',
    'memory_router',
    'realtime_router',
    'system_router',
    'tasks_router',
    'tools_router',
    'workflows_router',
]
