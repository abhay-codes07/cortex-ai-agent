from fastapi import APIRouter

from app.api.v1 import agents, collaboration, health, memory, realtime, system, tasks, tools, workflows
from app.core.config import settings

router = APIRouter()
router.include_router(health.router, tags=['health'])
router.include_router(system.router, prefix=settings.api_v1_prefix, tags=['system'])
router.include_router(agents.router, prefix=settings.api_v1_prefix, tags=['agents'])
router.include_router(realtime.router, prefix=settings.api_v1_prefix, tags=['realtime'])
router.include_router(tools.router, prefix=settings.api_v1_prefix, tags=['tools'])
router.include_router(memory.router, prefix=settings.api_v1_prefix, tags=['memory'])
router.include_router(collaboration.router, prefix=settings.api_v1_prefix, tags=['collaboration'])
router.include_router(workflows.router, prefix=settings.api_v1_prefix, tags=['workflows'])
router.include_router(tasks.router, prefix=settings.api_v1_prefix, tags=['tasks'])
