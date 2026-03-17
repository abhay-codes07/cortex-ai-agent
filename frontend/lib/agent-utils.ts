import type { AgentNode } from './types';

export function statusFromStage(stage: string): AgentNode['status'] {
  if (stage.includes('completed')) return 'done';
  if (stage.includes('decid') || stage.includes('orchestr') || stage.includes('planning')) return 'thinking';
  if (stage.includes('execut') || stage.includes('tool')) return 'working';
  return 'ready';
}

export function roleFromStage(stage: string): string | null {
  const known = ['orchestrator', 'planner', 'research', 'decision', 'execution', 'memory'];
  const matched = known.find((role) => stage.includes(role));
  return matched ?? null;
}
