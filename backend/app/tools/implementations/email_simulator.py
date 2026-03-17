from app.tools.base import BaseTool, ToolResult


class EmailSimulatorTool(BaseTool):
    def __init__(self) -> None:
        super().__init__(name='send_email', description='Simulates sending an execution summary email')

    def run(self, payload: dict) -> ToolResult:
        recipient = payload.get('recipient', 'ops@cortex.ai')
        subject = payload.get('subject', 'Cortex execution update')
        body = payload.get('body', 'Execution completed.')
        return ToolResult(
            tool=self.name,
            status='ok',
            output={
                'recipient': recipient,
                'subject': subject,
                'preview': body[:120],
                'message_id': 'email-sim-001',
            },
        )
