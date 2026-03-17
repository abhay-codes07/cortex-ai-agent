from fastapi import APIRouter

router = APIRouter()


@router.get('/health')
def health_check() -> dict[str, str]:
    return {'status': 'ok', 'service': 'cortex-backend'}


@router.get('/api/v1/status')
def app_status() -> dict[str, str]:
    return {'phase': '3', 'message': 'Agent base system online'}


@router.get('/api/v1/meta')
def app_meta() -> dict[str, str | list[str]]:
    return {
        'product': 'Cortex',
        'mode': 'phase-3-agent-foundation',
        'next': ['orchestrator-planner', 'memory-system', 'tool-execution'],
    }
