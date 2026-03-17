from fastapi import APIRouter

from app.services.system_service import SystemService

router = APIRouter()


@router.get('/system')
def system_health() -> dict[str, str]:
    service = SystemService()
    return service.overall_status()
