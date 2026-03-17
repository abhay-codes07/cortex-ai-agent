from collections.abc import Callable

from app.agents.collaboration.coordinator import CollaborationCoordinator
from app.agents.context import RuntimeContext
from app.agents.registry import AgentRegistry
from app.agents.sequence import DEFAULT_AGENT_SEQUENCE
from app.agents.transcript import CollaborationTranscript
from app.agents.types import AgentRole


class AgentRuntime:
    def __init__(self, registry: AgentRegistry):
        self.registry = registry
        self.sequence = DEFAULT_AGENT_SEQUENCE
        self.collaboration = CollaborationCoordinator(registry)

    def run_once(
        self,
        context: RuntimeContext,
        on_step: Callable[[AgentRole, RuntimeContext], None] | None = None,
    ) -> CollaborationTranscript:
        transcript = CollaborationTranscript()
        for role in self.sequence:
            if on_step:
                on_step(role, context)
            agent = self.registry.require(role)
            result = agent.run(context)
            transcript.add_result(result)
        return transcript

    def run_collaborative(
        self,
        context: RuntimeContext,
        rounds: int = 2,
        on_step: Callable[[AgentRole, RuntimeContext, int], None] | None = None,
    ) -> tuple[dict, CollaborationTranscript]:
        session, transcript = self.collaboration.run(context=context, rounds=rounds, on_step=on_step)
        return session.to_dict(), transcript
