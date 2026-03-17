from app.tools.base import BaseTool, ToolResult


class WebSearchMockTool(BaseTool):
    def __init__(self) -> None:
        super().__init__(name='web_search', description='Mock web search for strategy context')

    def run(self, payload: dict) -> ToolResult:
        query = payload.get('query', 'startup launch strategy')
        results = [
            {'title': 'Fast launch playbook', 'snippet': 'Ship quickly with narrow milestones.'},
            {'title': 'Execution scorecards', 'snippet': 'Track progress with clear ownership.'},
            {'title': 'Stakeholder updates', 'snippet': 'Use concise daily updates for trust.'},
        ]
        return ToolResult(tool=self.name, status='ok', output={'query': query, 'results': results})
