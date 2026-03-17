import uuid
from collections.abc import Callable

from app.agents.collaboration.message_bus import CollaborationMessageBus
from app.agents.collaboration.session import CollaborationSession
from app.agents.context import RuntimeContext
from app.agents.registry import AgentRegistry
from app.agents.sequence import DEFAULT_AGENT_SEQUENCE
from app.agents.transcript import CollaborationTranscript
from app.agents.types import AgentRole


class CollaborationCoordinator:
    def __init__(self, registry: AgentRegistry):
        self.registry = registry
        self.sequence = DEFAULT_AGENT_SEQUENCE

    def run(
        self,
        context: RuntimeContext,
        rounds: int = 2,
        on_step: Callable[[AgentRole, RuntimeContext, int], None] | None = None,
    ) -> tuple[CollaborationSession, CollaborationTranscript]:
        session = CollaborationSession(
            session_id=str(uuid.uuid4()),
            task_id=context.task_id,
            objective=context.objective,
            rounds=rounds,
        )
        transcript = CollaborationTranscript()
        bus = CollaborationMessageBus()

        context.set_state('collaboration_rounds', rounds)
        context.set_state('collaboration_session_id', session.session_id)

        for round_index in range(1, rounds + 1):
            session.add_event('round_start', f'Round {round_index} started', {'round': round_index})
            context.add_timeline_event('collaboration', f'Round {round_index} started', {'round': round_index})

            for role in self.sequence:
                inbox = bus.drain_for(role)
                context.set_state(f'inbox:{role.value}', [message.model_dump(mode='json') for message in inbox])
                context.set_state(f'round:{role.value}', round_index)

                if on_step:
                    on_step(role, context, round_index)

                agent = self.registry.require(role)
                result = agent.run(context)
                transcript.add_result(result)
                session.add_result(result)
                bus.publish_many(result.messages)

                session.add_event(
                    'agent_turn',
                    f'{role.value} completed round {round_index}',
                    {
                        'round': round_index,
                        'thoughts': len(result.thoughts),
                        'actions': len(result.actions),
                        'messages': len(result.messages),
                    },
                )

            session.add_event('round_end', f'Round {round_index} completed', {'round': round_index})
            context.add_timeline_event('collaboration', f'Round {round_index} completed', {'round': round_index})

        pending = bus.all_messages()
        context.set_state('collaboration_pending_messages', [message.model_dump(mode='json') for message in pending])
        session.add_event('session_complete', 'Collaboration session completed', {'pending_messages': len(pending)})

        return session, transcript
