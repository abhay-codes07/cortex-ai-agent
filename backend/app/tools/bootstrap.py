from app.tools.implementations.email_simulator import EmailSimulatorTool
from app.tools.implementations.slack_simulator import SlackSimulatorTool
from app.tools.implementations.task_executor import TaskExecutorTool
from app.tools.implementations.web_search_mock import WebSearchMockTool
from app.tools.registry import ToolRegistry


def build_tool_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(EmailSimulatorTool())
    registry.register(SlackSimulatorTool())
    registry.register(WebSearchMockTool())
    registry.register(TaskExecutorTool())
    return registry
