from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db_session
from app.schemas.collaboration import CollaborationRunRequest, CollaborationRunResponse, CollaborationSessionsResponse
from app.services.collaboration_service import CollaborationService

router = APIRouter(prefix='/collaboration')


def get_collaboration_service(db: Session = Depends(get_db_session)) -> CollaborationService:
    return CollaborationService(db)


@router.post('/run', response_model=CollaborationRunResponse, status_code=status.HTTP_200_OK)
def run_collaboration(
    payload: CollaborationRunRequest,
    service: CollaborationService = Depends(get_collaboration_service),
) -> CollaborationRunResponse:
    try:
        return service.run(payload)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get('/sessions', response_model=CollaborationSessionsResponse, status_code=status.HTTP_200_OK)
def list_collaboration_sessions(
    service: CollaborationService = Depends(get_collaboration_service),
) -> CollaborationSessionsResponse:
    return service.sessions()
