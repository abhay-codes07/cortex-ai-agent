from fastapi import APIRouter

from app.api.v1 import agents, health, system, tasks
from app.core.config import settings

router = APIRouter()
router.include_router(health.router, tags=['health'])
router.include_router(system.router, prefix=settings.api_v1_prefix, tags=['system'])
router.include_router(agents.router, prefix=settings.api_v1_prefix, tags=['agents'])
router.include_router(tasks.router, prefix=settings.api_v1_prefix, tags=['tasks'])
