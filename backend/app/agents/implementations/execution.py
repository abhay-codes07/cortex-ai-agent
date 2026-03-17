from app.agents.base import BaseAgent
from app.agents.context import RuntimeContext
from app.agents.contracts import AgentResult
from app.agents.prompt_templates import EXECUTION_PROMPT
from app.agents.types import AgentRole


class ExecutionAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(role=AgentRole.execution, name='Execution Agent')

    def run(self, context: RuntimeContext) -> AgentResult:
        strategy = context.get_state('selected_strategy', {})
        milestones = context.recall('plan_milestones', [])

        tool_executor = context.get_state('tool_executor')
        tool_results: list[dict] = []

        if callable(tool_executor):
            tool_results.append(
                tool_executor(
                    'web_search',
                    {'query': f"{context.objective} execution strategy"},
                ).model_dump(mode='json')
            )

            for milestone in milestones[:3]:
                tool_results.append(
                    tool_executor(
                        'execute_task',
                        {'task_name': milestone.get('title', 'Execute milestone'), 'owner': milestone.get('owner', 'Execution Agent')},
                    ).model_dump(mode='json')
                )

            tool_results.append(
                tool_executor(
                    'send_slack',
                    {'channel': '#cortex-live', 'message': 'Execution milestones completed. Packaging final output.'},
                ).model_dump(mode='json')
            )
            tool_results.append(
                tool_executor(
                    'send_email',
                    {
                        'recipient': 'founder@cortex.ai',
                        'subject': 'Cortex Workflow Complete',
                        'body': 'Execution lane completed with milestone evidence and timeline logs.',
                    },
                ).model_dump(mode='json')
            )

        deliverables = [
            'Objective interpreted and execution lane activated',
            'Milestones completed with status evidence',
            'Final output packaged for stakeholder review',
        ]

        if milestones:
            deliverables.append(f"Executed {len(milestones)} planned milestones in coordinated sequence")
        if tool_results:
            deliverables.append(f"Executed {len(tool_results)} tool operations through tool abstraction layer")

        thought = self.thought(
            step='Execute selected strategy',
            reasoning=f'{EXECUTION_PROMPT} Applying strategy into concrete deliverables with milestone-level completion evidence.',
        )
        action = self.action(
            'execute_plan',
            {
                'strategy': strategy.get('strategy', 'default'),
                'deliverables': deliverables,
                'tool_calls': len(tool_results),
            },
        )
        message = self.message(AgentRole.memory, 'Store execution context and outcomes for future recall.')

        context.set_state('deliverables', deliverables)
        context.set_state('tool_results', tool_results)
        context.add_timeline_event(
            'executing',
            'Execution agent completed deliverable run',
            {'deliverables': len(deliverables), 'tool_calls': len(tool_results)},
        )

        return AgentResult(
            agent=self.role,
            status='ok',
            output={'deliverables': deliverables, 'tool_results': tool_results},
            thoughts=[thought],
            actions=[action],
            messages=[message],
        )
