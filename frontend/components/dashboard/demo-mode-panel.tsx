"use client";

import { WandSparkles } from 'lucide-react';

import type { DemoScenario } from '@/lib/types';

type DemoModePanelProps = {
  scenarios: DemoScenario[];
  selectedScenarioId: string;
  onSelectScenario: (scenarioId: string) => void;
  onRunScenario: () => void;
  running: boolean;
};

export function DemoModePanel({
  scenarios,
  selectedScenarioId,
  onSelectScenario,
  onRunScenario,
  running,
}: DemoModePanelProps) {
  return (
    <section className="glass-panel rounded-2xl p-4">
      <div className="mb-3 flex items-center justify-between">
        <h2 className="inline-flex items-center gap-2 text-base font-semibold">
          <WandSparkles className="h-4 w-4 text-[#ff8b42]" />
          Demo Autopilot
        </h2>
        <span className="mono text-[11px] uppercase tracking-[0.2em] text-[#91a7c9]">phase 10</span>
      </div>
      <div className="space-y-2">
        {scenarios.map((scenario) => (
          <button
            key={scenario.id}
            type="button"
            onClick={() => onSelectScenario(scenario.id)}
            className={`w-full rounded-lg border px-3 py-2 text-left text-xs transition ${
              selectedScenarioId === scenario.id
                ? 'border-[#4aa8ff]/60 bg-[#4aa8ff]/20 text-white'
                : 'border-white/15 bg-white/5 text-[#c8d8ee] hover:bg-white/10'
            }`}
          >
            <p className="font-semibold">{scenario.title}</p>
            <p className="mt-1 text-[11px] text-[#a9bad2]">{scenario.objective.slice(0, 110)}</p>
          </button>
        ))}
      </div>
      <button
        type="button"
        disabled={running || !selectedScenarioId}
        onClick={onRunScenario}
        className="mt-3 w-full rounded-lg border border-[#1fd3b4]/50 bg-[#1fd3b4]/20 px-3 py-2 text-sm font-semibold transition hover:bg-[#1fd3b4]/30 disabled:cursor-not-allowed disabled:opacity-60"
      >
        Run One-Click Demo
      </button>
    </section>
  );
}
