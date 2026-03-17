from fastapi import APIRouter

router = APIRouter()


@router.get('/health')
def health_check() -> dict[str, str]:
    return {'status': 'ok', 'service': 'cortex-backend'}


@router.get('/api/v1/status')
def app_status() -> dict[str, str]:
    return {'phase': '1', 'message': 'Backend scaffold ready'}
