from app.tools.base import BaseTool


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> BaseTool | None:
        return self._tools.get(name)

    def require(self, name: str) -> BaseTool:
        tool = self.get(name)
        if not tool:
            raise ValueError(f'Tool not registered: {name}')
        return tool

    def list_tools(self) -> list[dict[str, str]]:
        return [{'name': tool.name, 'description': tool.description} for tool in self._tools.values()]
