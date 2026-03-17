from fastapi import APIRouter

router = APIRouter()


@router.get('/health')
def health_check() -> dict[str, str]:
    return {'status': 'ok', 'service': 'cortex-backend'}


@router.get('/api/v1/status')
def app_status() -> dict[str, str]:
    return {'phase': '2', 'message': 'Backend core APIs online'}


@router.get('/api/v1/meta')
def app_meta() -> dict[str, str | list[str]]:
    return {
        'product': 'Cortex',
        'mode': 'phase-2-backend-core',
        'next': ['agent-base-system', 'orchestrator-planner', 'memory-system'],
    }
