export type AgentNode = {
  role: string;
  name: string;
  status: 'idle' | 'thinking' | 'working' | 'done' | 'ready';
};

export type TimelineEvent = {
  stage: string;
  message: string;
  timestamp?: string;
  metadata?: Record<string, unknown>;
};

export type WorkflowRunResponse = {
  task: {
    id: string;
    title: string;
    prompt: string;
    status: string;
    result?: string | null;
  };
  mode: string;
  timeline: TimelineEvent[];
  transcript: {
    thoughts: Array<{ agent: string; step: string; reasoning: string }>;
    actions: Array<{ agent: string; action: string; payload: Record<string, unknown> }>;
    messages: Array<{ from_agent: string; to_agent: string; content: string }>;
  };
  plan_overview: string[];
};

export type CollaborationRunResponse = {
  task_id: string;
  objective: string;
  rounds: number;
  session: {
    session_id: string;
    events: TimelineEvent[];
  };
  timeline: TimelineEvent[];
  transcript: WorkflowRunResponse['transcript'];
};

export type MemoryRecallItem = {
  summary: string;
  workflow_mode: string;
  strategy?: string | null;
  relevance_score?: number | null;
};
