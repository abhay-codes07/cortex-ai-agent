from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db_session
from app.schemas.demo import DemoRunRequest, DemoRunResponse, DemoScenariosResponse
from app.services.demo_service import DemoService

router = APIRouter(prefix='/demo')


def get_demo_service(db: Session = Depends(get_db_session)) -> DemoService:
    return DemoService(db)


@router.get('/scenarios', response_model=DemoScenariosResponse, status_code=status.HTTP_200_OK)
def demo_scenarios(service: DemoService = Depends(get_demo_service)) -> DemoScenariosResponse:
    return service.scenarios()


@router.post('/run', response_model=DemoRunResponse, status_code=status.HTTP_200_OK)
def run_demo(payload: DemoRunRequest, service: DemoService = Depends(get_demo_service)) -> DemoRunResponse:
    return service.run(payload)
