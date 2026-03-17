from datetime import datetime

from app.agents.base import BaseAgent
from app.agents.context import RuntimeContext
from app.agents.contracts import AgentResult
from app.agents.prompt_templates import MEMORY_PROMPT
from app.agents.types import AgentRole


class MemoryAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(role=AgentRole.memory, name='Memory Agent')

    def run(self, context: RuntimeContext) -> AgentResult:
        snapshot = {
            'task_id': context.task_id,
            'objective': context.objective,
            'plan_steps': context.recall('plan_steps', []),
            'deliverables': context.get_state('deliverables', []),
            'captured_at': datetime.utcnow().isoformat(),
        }

        thought = self.thought(
            step='Persist context snapshot',
            reasoning=f'{MEMORY_PROMPT} Capturing short-term memory and execution outputs for downstream long-term storage.',
        )
        action = self.action('save_memory_snapshot', {'keys': list(snapshot.keys())})

        context.remember('memory_snapshot', snapshot)

        return AgentResult(
            agent=self.role,
            status='ok',
            output={'snapshot': snapshot},
            thoughts=[thought],
            actions=[action],
            messages=[],
        )
