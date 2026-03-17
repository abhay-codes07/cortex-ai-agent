from app.tools.base import BaseTool, ToolResult


class SlackSimulatorTool(BaseTool):
    def __init__(self) -> None:
        super().__init__(name='send_slack', description='Simulates posting an update to Slack')

    def run(self, payload: dict) -> ToolResult:
        channel = payload.get('channel', '#ai-workforce')
        message = payload.get('message', 'Workflow update available.')
        return ToolResult(
            tool=self.name,
            status='ok',
            output={
                'channel': channel,
                'message_preview': message[:140],
                'post_id': 'slack-sim-001',
            },
        )
