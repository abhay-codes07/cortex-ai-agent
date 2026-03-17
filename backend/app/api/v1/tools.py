from fastapi import APIRouter, Depends, status

from app.schemas.tool import (
    ToolBatchExecuteRequest,
    ToolBatchExecuteResponse,
    ToolDescriptor,
    ToolExecuteRequest,
    ToolExecuteResponse,
)
from app.services.tool_service import ToolService

router = APIRouter(prefix='/tools')


def get_tool_service() -> ToolService:
    return ToolService()


@router.get('', response_model=list[ToolDescriptor])
def list_tools(service: ToolService = Depends(get_tool_service)) -> list[ToolDescriptor]:
    return service.list_tools()


@router.post('/execute', response_model=ToolExecuteResponse, status_code=status.HTTP_200_OK)
def execute_tool(
    payload: ToolExecuteRequest,
    service: ToolService = Depends(get_tool_service),
) -> ToolExecuteResponse:
    return service.execute(payload)


@router.post('/execute/batch', response_model=ToolBatchExecuteResponse, status_code=status.HTTP_200_OK)
def execute_tools(
    payload: ToolBatchExecuteRequest,
    service: ToolService = Depends(get_tool_service),
) -> ToolBatchExecuteResponse:
    return service.execute_batch(payload)
