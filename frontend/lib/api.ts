import type {
  CollaborationRunResponse,
  MemoryRecallItem,
  WorkflowRunResponse,
} from './types';

const BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://localhost:8000';

async function callApi<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${BASE_URL}${path}`, {
    ...init,
    headers: {
      'Content-Type': 'application/json',
      ...(init?.headers || {}),
    },
    cache: 'no-store',
  });

  if (!response.ok) {
    throw new Error(`API ${response.status}: ${path}`);
  }

  return (await response.json()) as T;
}

export async function runWorkflow(objective: string): Promise<WorkflowRunResponse> {
  return callApi<WorkflowRunResponse>('/api/v1/workflows/run', {
    method: 'POST',
    body: JSON.stringify({
      title: objective.slice(0, 80),
      objective,
    }),
  });
}

export async function runCollaboration(objective: string, rounds = 2): Promise<CollaborationRunResponse> {
  return callApi<CollaborationRunResponse>('/api/v1/collaboration/run', {
    method: 'POST',
    body: JSON.stringify({
      title: objective.slice(0, 80),
      objective,
      rounds,
    }),
  });
}

export async function listAgents(): Promise<Array<{ role: string; name: string; status: string }>> {
  const data = await callApi<{ count: number; items: Array<{ role: string; name: string; status: string }> }>(
    '/api/v1/agents',
  );
  return data.items;
}

export async function recallMemory(objective: string): Promise<MemoryRecallItem[]> {
  const data = await callApi<{ items: MemoryRecallItem[] }>('/api/v1/memory/recall', {
    method: 'POST',
    body: JSON.stringify({ objective, limit: 3 }),
  });
  return data.items;
}

export async function recentTasks(): Promise<Array<{ id: string; title: string; status: string; created_at: string }>> {
  const data = await callApi<{
    items: Array<{ id: string; title: string; status: string; created_at: string }>;
  }>('/api/v1/tasks?limit=8&offset=0');
  return data.items;
}
