"use client";

import { useEffect, useMemo, useRef, useState } from 'react';
import { motion } from 'framer-motion';
import Link from 'next/link';
import { BrainCircuit, Home, RadioTower } from 'lucide-react';

import { AgentNetwork } from '@/components/dashboard/agent-network';
import { DemoModePanel } from '@/components/dashboard/demo-mode-panel';
import { LogStream } from '@/components/dashboard/log-stream';
import { MemoryPanel } from '@/components/dashboard/memory-panel';
import { MetricChip } from '@/components/dashboard/metric-chip';
import { TaskComposer } from '@/components/dashboard/task-composer';
import { TaskHistory } from '@/components/dashboard/task-history';
import { TimelinePanel } from '@/components/dashboard/timeline-panel';
import { roleFromStage, statusFromStage } from '@/lib/agent-utils';
import {
  demoScenarios,
  listAgents,
  recallMemory,
  recentTasks,
  runCollaboration,
  runDemoScenario,
  runWorkflow,
} from '@/lib/api';
import { DEMO_TASKS, mockCollaborationResponse, mockWorkflowResponse } from '@/lib/demo';
import { extractTimelineFromDemoResult } from '@/lib/demo-utils';
import { connectRealtime, type RealtimeConnectionState } from '@/lib/realtime';
import type { AgentNode, DemoScenario, MemoryRecallItem, TimelineEvent } from '@/lib/types';

const fallbackAgents: AgentNode[] = [
  { role: 'orchestrator', name: 'Orchestrator Agent', status: 'ready' },
  { role: 'planner', name: 'Planner Agent', status: 'ready' },
  { role: 'research', name: 'Research Agent', status: 'ready' },
  { role: 'decision', name: 'Decision Agent', status: 'ready' },
  { role: 'execution', name: 'Execution Agent', status: 'ready' },
  { role: 'memory', name: 'Memory Agent', status: 'ready' },
];

const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

export default function DashboardPage() {
  const [objective, setObjective] = useState(DEMO_TASKS[0]);
  const [demoMode, setDemoMode] = useState(true);
  const [running, setRunning] = useState(false);

  const [agents, setAgents] = useState<AgentNode[]>(fallbackAgents);
  const [logs, setLogs] = useState<string[]>([]);
  const [timeline, setTimeline] = useState<TimelineEvent[]>([]);
  const [memoryItems, setMemoryItems] = useState<MemoryRecallItem[]>([]);
  const [history, setHistory] = useState<Array<{ id: string; title: string; status: string; created_at: string }>>([]);

  const [runMode, setRunMode] = useState<'workflow' | 'collaboration' | 'autopilot'>('workflow');
  const [realtimeState, setRealtimeState] = useState<RealtimeConnectionState>('disconnected');
  const [scenarios, setScenarios] = useState<DemoScenario[]>([]);
  const [selectedScenarioId, setSelectedScenarioId] = useState('');

  const socketRef = useRef<WebSocket | null>(null);
  const liveEventCounterRef = useRef(0);

  const stats = useMemo(() => {
    const done = agents.filter((agent) => agent.status === 'done').length;
    const working = agents.filter((agent) => agent.status === 'working' || agent.status === 'thinking').length;
    return { done, working, total: agents.length };
  }, [agents]);

  useEffect(() => {
    const bootstrap = async () => {
      try {
        const [agentRows, tasks, scenarioRows] = await Promise.all([listAgents(), recentTasks(), demoScenarios()]);
        setAgents(
          agentRows.map((agent) => ({
            role: agent.role,
            name: agent.name,
            status: (agent.status as AgentNode['status']) || 'ready',
          })),
        );
        setHistory(tasks);
        setScenarios(scenarioRows);
        if (scenarioRows[0]) setSelectedScenarioId(scenarioRows[0].id);
      } catch {
        setLogs((prev) => [...prev, '[bootstrap] API unreachable, using local demo profile']);
      }
    };

    void bootstrap();
  }, []);

  useEffect(() => {
    const socket = connectRealtime({
      onStateChange: (state) => setRealtimeState(state),
      onEvent: (event) => {
        liveEventCounterRef.current += 1;

        if (!running || demoMode) return;

        setTimeline((prev) => [...prev, event]);
        setLogs((prev) => [...prev, `[${event.stage}] ${event.message}`]);

        setAgents((prev) =>
          prev.map((agent) => {
            const role = roleFromStage(event.stage);
            if (role && role === agent.role) {
              return { ...agent, status: statusFromStage(event.stage) };
            }
            return agent;
          }),
        );
      },
    });

    socketRef.current = socket;

    const ping = setInterval(() => {
      if (socket.readyState === WebSocket.OPEN) {
        socket.send('ping');
      }
    }, 15000);

    return () => {
      clearInterval(ping);
      socket.close();
    };
  }, [demoMode, running]);

  const streamExperience = async (events: TimelineEvent[]) => {
    setTimeline([]);
    for (let index = 0; index < events.length; index += 1) {
      const event = events[index];
      setTimeline((prev) => [...prev, event]);
      setLogs((prev) => [...prev, `[${event.stage}] ${event.message}`]);

      setAgents((prev) =>
        prev.map((agent) => {
          const role = roleFromStage(event.stage);
          if (role && role === agent.role) {
            return { ...agent, status: statusFromStage(event.stage) };
          }
          return agent;
        }),
      );
      await sleep(100);
    }
    setAgents((prev) => prev.map((agent) => ({ ...agent, status: 'done' })));
  };

  const runMission = async () => {
    if (!objective.trim()) return;

    setRunning(true);
    setLogs([`[mission] ${objective}`]);
    setTimeline([]);
    setAgents((prev) => prev.map((agent) => ({ ...agent, status: 'thinking' })));

    try {
      const memory = demoMode ? [] : await recallMemory(objective);
      setMemoryItems(memory);

      const beforeCounter = liveEventCounterRef.current;
      const workflow = demoMode ? mockWorkflowResponse(objective) : await runWorkflow(objective);

      if (demoMode) {
        await streamExperience(workflow.timeline);
      } else if (liveEventCounterRef.current === beforeCounter || realtimeState !== 'connected') {
        await streamExperience(workflow.timeline);
      }

      setLogs((prev) => [...prev, `[result] ${workflow.task.result ?? 'Mission complete'}`]);
      setRunMode('workflow');
    } catch {
      const fallback = mockWorkflowResponse(objective);
      setLogs((prev) => [...prev, '[fallback] Backend unavailable. Running deterministic demo.']);
      await streamExperience(fallback.timeline);
      setRunMode('workflow');
    } finally {
      setRunning(false);
      if (!demoMode) {
        try {
          const tasks = await recentTasks();
          setHistory(tasks);
        } catch {
          // Keep existing history if API is unavailable.
        }
      }
    }
  };

  const runAutoDemo = async () => {
    const selected = DEMO_TASKS[Math.floor(Math.random() * DEMO_TASKS.length)];
    setObjective(selected);
    setRunning(true);
    setLogs([`[demo] ${selected}`]);
    setTimeline([]);
    setAgents((prev) => prev.map((agent) => ({ ...agent, status: 'thinking' })));

    try {
      const beforeCounter = liveEventCounterRef.current;
      const result = demoMode ? mockCollaborationResponse(selected) : await runCollaboration(selected, 2);

      if (demoMode) {
        await streamExperience(result.timeline);
      } else if (liveEventCounterRef.current === beforeCounter || realtimeState !== 'connected') {
        await streamExperience(result.timeline);
      }

      setLogs((prev) => [...prev, `[collaboration] session complete in ${result.rounds} rounds`]);
      setRunMode('collaboration');
    } catch {
      const fallback = mockCollaborationResponse(selected);
      setLogs((prev) => [...prev, '[fallback] Collaboration API unreachable. Showing scripted demo run.']);
      await streamExperience(fallback.timeline);
      setRunMode('collaboration');
    } finally {
      setRunning(false);
    }
  };

  const runAutopilot = async () => {
    if (!selectedScenarioId) return;

    setRunning(true);
    setTimeline([]);
    setAgents((prev) => prev.map((agent) => ({ ...agent, status: 'thinking' })));
    setLogs((prev) => [...prev, `[autopilot] launching scenario ${selectedScenarioId}`]);

    try {
      const beforeCounter = liveEventCounterRef.current;
      const result = await runDemoScenario(selectedScenarioId);
      const events = extractTimelineFromDemoResult(result.result);

      if (liveEventCounterRef.current === beforeCounter || realtimeState !== 'connected') {
        await streamExperience(events.length > 0 ? events : mockWorkflowResponse(result.scenario.objective).timeline);
      }

      setObjective(result.scenario.objective);
      setRunMode('autopilot');
      setLogs((prev) => [...prev, `[autopilot] scenario complete: ${result.scenario.title}`]);

      try {
        const tasks = await recentTasks();
        setHistory(tasks);
      } catch {
        // Keep history unchanged.
      }
    } catch {
      setLogs((prev) => [...prev, '[autopilot] backend unavailable, switching to deterministic fallback']);
      const fallback = mockCollaborationResponse(objective);
      await streamExperience(fallback.timeline);
      setRunMode('autopilot');
    } finally {
      setRunning(false);
    }
  };

  return (
    <main className="cortex-grid min-h-screen px-4 py-6 md:px-10 md:py-8">
      <section className="mx-auto flex w-full max-w-[1400px] flex-col gap-5">
        <motion.header
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          className="glass-panel flex flex-wrap items-center justify-between gap-4 rounded-2xl px-5 py-4"
        >
          <div>
            <p className="mono text-xs uppercase tracking-[0.22em] text-[#a7c7f6]">Cortex Command Center</p>
            <h1 className="mt-1 text-2xl font-bold md:text-3xl">Autonomous AI Workforce Dashboard</h1>
          </div>
          <div className="flex flex-wrap items-center gap-2 text-sm text-[#c9d8ef]">
            <MetricChip label="Active" value={String(stats.working)} tone="mint" />
            <MetricChip label="Done" value={`${stats.done}/${stats.total}`} tone="sky" />
            <MetricChip label="Mode" value={runMode} tone="amber" />
            <span className="inline-flex items-center gap-2 rounded-lg border border-white/15 bg-white/5 px-3 py-1.5">
              <RadioTower className={`h-4 w-4 ${realtimeState === 'connected' ? 'text-[#1fd3b4]' : 'text-[#ff8b42]'}`} />
              <span className="mono text-xs uppercase tracking-[0.18em]">{realtimeState}</span>
            </span>
            <Link href="/" className="inline-flex items-center gap-2 rounded-lg border border-white/15 bg-white/5 px-3 py-1.5 hover:bg-white/10">
              <Home className="h-4 w-4" />
              Home
            </Link>
          </div>
        </motion.header>

        <TaskComposer
          value={objective}
          onChange={setObjective}
          onRun={() => void runMission()}
          onDemo={() => void runAutoDemo()}
          running={running}
          demoMode={demoMode}
          onToggleDemo={() => setDemoMode((prev) => !prev)}
        />

        <div className="grid gap-4 lg:grid-cols-3">
          <div className="lg:col-span-2">
            <div className="flex flex-wrap gap-2">
              {DEMO_TASKS.map((task) => (
                <button
                  key={task}
                  type="button"
                  onClick={() => setObjective(task)}
                  className="rounded-lg border border-white/15 bg-white/5 px-3 py-1.5 text-xs text-[#d4e0f4] hover:bg-white/10"
                >
                  {task.slice(0, 74)}
                </button>
              ))}
            </div>
          </div>
          <DemoModePanel
            scenarios={scenarios}
            selectedScenarioId={selectedScenarioId}
            onSelectScenario={setSelectedScenarioId}
            onRunScenario={() => void runAutopilot()}
            running={running}
          />
        </div>

        <div className="grid gap-4 xl:grid-cols-3">
          <div className="space-y-4 xl:col-span-2">
            <AgentNetwork nodes={agents} />
            <TimelinePanel events={timeline} />
          </div>
          <div className="space-y-4">
            <LogStream logs={logs} />
            <div className="glass-panel rounded-2xl p-4">
              <p className="mono text-xs uppercase tracking-[0.2em] text-[#95a9c8]">Current Run Mode</p>
              <p className="mt-2 inline-flex items-center gap-2 text-sm">
                <BrainCircuit className="h-4 w-4 text-[#ff8b42]" />
                {runMode}
              </p>
            </div>
          </div>
        </div>

        <div className="grid gap-4 lg:grid-cols-2">
          <MemoryPanel items={memoryItems} />
          <TaskHistory items={history} />
        </div>
      </section>
    </main>
  );
}
