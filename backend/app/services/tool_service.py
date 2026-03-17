from app.schemas.tool import (
    ToolBatchExecuteRequest,
    ToolBatchExecuteResponse,
    ToolDescriptor,
    ToolExecuteRequest,
    ToolExecuteResponse,
)
from app.tools import build_tool_registry


class ToolService:
    def __init__(self) -> None:
        self.registry = build_tool_registry()

    def list_tools(self) -> list[ToolDescriptor]:
        return [ToolDescriptor(**tool) for tool in self.registry.list_tools()]

    def execute(self, payload: ToolExecuteRequest) -> ToolExecuteResponse:
        tool = self.registry.require(payload.name)
        result = tool.run(payload.payload)
        return ToolExecuteResponse(**result.model_dump())

    def execute_batch(self, payload: ToolBatchExecuteRequest) -> ToolBatchExecuteResponse:
        results = [self.execute(call) for call in payload.calls]
        return ToolBatchExecuteResponse(results=results, count=len(results))

    def execute_tool(self, name: str, data: dict) -> ToolExecuteResponse:
        return self.execute(ToolExecuteRequest(name=name, payload=data))
