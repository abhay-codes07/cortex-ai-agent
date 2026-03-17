from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db_session
from app.schemas.workflow import WorkflowRunRequest, WorkflowRunResponse
from app.services.workflow_service import WorkflowService

router = APIRouter(prefix='/workflows')


def get_workflow_service(db: Session = Depends(get_db_session)) -> WorkflowService:
    return WorkflowService(db)


@router.post('/run', response_model=WorkflowRunResponse, status_code=status.HTTP_200_OK)
def run_workflow(
    payload: WorkflowRunRequest,
    service: WorkflowService = Depends(get_workflow_service),
) -> WorkflowRunResponse:
    try:
        return service.run(payload)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
