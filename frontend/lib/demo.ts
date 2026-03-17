import type { CollaborationRunResponse, TimelineEvent, WorkflowRunResponse } from './types';

const baseTimeline: TimelineEvent[] = [
  { stage: 'orchestrating', message: 'Orchestrator selected workflow mode: parallel-fastlane' },
  { stage: 'planning', message: 'Planner generated milestone plan with ownership mapping' },
  { stage: 'researching', message: 'Research agent synthesized evidence and context' },
  { stage: 'deciding', message: 'Decision agent selected high-confidence execution strategy' },
  { stage: 'tool_execution', message: 'Execution agent invoked web_search and execute_task tools' },
  { stage: 'executing', message: 'Execution lane completed with validated deliverables' },
  { stage: 'memory_sync', message: 'Memory agent captured long-term recall snapshot' },
  { stage: 'completed', message: 'Workflow completed successfully' },
];

export function mockWorkflowResponse(objective: string): WorkflowRunResponse {
  return {
    task: {
      id: `demo-${Date.now()}`,
      title: objective.slice(0, 80),
      prompt: objective,
      status: 'completed',
      result: 'Demo workflow completed with visible multi-agent collaboration.',
    },
    mode: 'parallel-fastlane',
    timeline: baseTimeline,
    plan_overview: [
      '1. Define success criteria and constraints (Planner Agent)',
      '2. Collect evidence and options (Research Agent)',
      '3. Select execution strategy (Decision Agent)',
      '4. Execute milestones and package output (Execution Agent)',
    ],
    transcript: {
      thoughts: [
        { agent: 'orchestrator', step: 'Coordinate workflow', reasoning: 'Selected parallel-fastlane for high-urgency objective.' },
        { agent: 'planner', step: 'Break objective into plan', reasoning: 'Mapped owners and milestones for execution speed.' },
        { agent: 'execution', step: 'Execute selected strategy', reasoning: 'Used tool layer to validate and complete deliverables.' },
      ],
      actions: [
        { agent: 'planner', action: 'draft_plan', payload: { milestones: 4 } },
        { agent: 'execution', action: 'execute_plan', payload: { tool_calls: 6 } },
      ],
      messages: [
        { from_agent: 'orchestrator', to_agent: 'planner', content: 'Generate rapid but reliable milestone plan.' },
        { from_agent: 'decision', to_agent: 'execution', content: 'Execute with visible checkpoints and tool traces.' },
      ],
    },
  };
}

export function mockCollaborationResponse(objective: string): CollaborationRunResponse {
  return {
    task_id: `collab-${Date.now()}`,
    objective,
    rounds: 2,
    session: {
      session_id: `session-${Date.now()}`,
      events: [
        { stage: 'round_start', message: 'Round 1 started' },
        { stage: 'agent_turn', message: 'planner completed round 1' },
        { stage: 'round_end', message: 'Round 1 completed' },
        { stage: 'round_start', message: 'Round 2 started' },
        { stage: 'agent_turn', message: 'execution completed round 2' },
        { stage: 'session_complete', message: 'Collaboration session completed' },
      ],
    },
    timeline: baseTimeline,
    transcript: {
      thoughts: [
        { agent: 'planner', step: 'Refine plan', reasoning: 'Used inbox feedback to improve sequencing.' },
        { agent: 'research', step: 'Validate assumptions', reasoning: 'Added supporting evidence for decision confidence.' },
      ],
      actions: [
        { agent: 'execution', action: 'execute_plan', payload: { tool_calls: 7, inbox_messages: 2 } },
      ],
      messages: [
        { from_agent: 'planner', to_agent: 'research', content: 'Prioritize validation on top 2 milestones.' },
        { from_agent: 'research', to_agent: 'decision', content: 'Evidence quality improved after round-one feedback.' },
      ],
    },
  };
}

export const DEMO_TASKS = [
  'Launch a 7-day growth sprint for Cortex with milestones, ownership, and execution logs.',
  'Plan and execute a product announcement campaign across email, Slack, and internal ops.',
  'Coordinate a cross-functional AI launch war-room and produce a final execution brief.',
];
