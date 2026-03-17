from fastapi import APIRouter

from app.schemas.agent import AgentSimulationRequest, AgentSimulationResponse
from app.services.agent_system_service import AgentSystemService

router = APIRouter(prefix='/agents')


@router.get('')
def list_agents() -> dict:
    service = AgentSystemService()
    nodes = service.list_nodes()
    return {'count': len(nodes), 'items': [node.model_dump(mode='json') for node in nodes]}


@router.post('/simulate', response_model=AgentSimulationResponse)
def simulate_agents(payload: AgentSimulationRequest) -> AgentSimulationResponse:
    service = AgentSystemService()
    return service.simulate(payload)
