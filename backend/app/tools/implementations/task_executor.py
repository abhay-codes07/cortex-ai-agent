from app.tools.base import BaseTool, ToolResult


class TaskExecutorTool(BaseTool):
    def __init__(self) -> None:
        super().__init__(name='execute_task', description='Simulates execution of a concrete milestone task')

    def run(self, payload: dict) -> ToolResult:
        task_name = payload.get('task_name', 'Execute milestone')
        owner = payload.get('owner', 'Execution Agent')
        return ToolResult(
            tool=self.name,
            status='ok',
            output={
                'task_name': task_name,
                'owner': owner,
                'status': 'completed',
                'evidence': f'{task_name} completed successfully by {owner}',
            },
        )
