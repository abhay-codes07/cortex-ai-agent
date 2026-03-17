# Agent Workflow (Phase 7)

1. Collaboration runtime initializes a session and shared message bus.
2. Agents run in multi-round cycles (default 2 rounds).
3. After each agent turn:
   - thoughts/actions are logged
   - inter-agent messages are published to the bus
   - next agent receives inbox from previous messages
4. Execution agent performs tool calls while collaboration is active.
5. Memory agent captures deliverables, tool outputs, and collaboration messages.
6. Session events and transcript are persisted in response payload for UI playback.

This creates visible agent-to-agent coordination beyond sequential single-pass execution.
