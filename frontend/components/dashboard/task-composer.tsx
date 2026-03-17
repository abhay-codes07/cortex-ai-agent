"use client";

import { Rocket, PlayCircle, Wand2 } from 'lucide-react';

type TaskComposerProps = {
  value: string;
  onChange: (value: string) => void;
  onRun: () => void;
  onDemo: () => void;
  running: boolean;
  demoMode: boolean;
  onToggleDemo: () => void;
};

export function TaskComposer({
  value,
  onChange,
  onRun,
  onDemo,
  running,
  demoMode,
  onToggleDemo,
}: TaskComposerProps) {
  return (
    <section className="glass-panel rounded-2xl p-5 md:p-6">
      <div className="mb-4 flex items-center justify-between gap-3">
        <h2 className="text-xl font-semibold">Mission Control</h2>
        <button
          type="button"
          onClick={onToggleDemo}
          className={`mono rounded-lg border px-3 py-1 text-xs uppercase tracking-wider transition ${
            demoMode
              ? 'border-[#1fd3b4]/60 bg-[#1fd3b4]/20 text-[#9cf4e3]'
              : 'border-white/20 bg-white/5 text-[#a7b6cd]'
          }`}
        >
          Demo Mode {demoMode ? 'On' : 'Off'}
        </button>
      </div>
      <textarea
        value={value}
        onChange={(event) => onChange(event.target.value)}
        placeholder="Give Cortex a mission..."
        className="h-32 w-full resize-none rounded-xl border border-white/15 bg-[#0f172a]/70 p-4 text-sm text-white outline-none transition focus:border-[#4aa8ff]/70"
      />
      <div className="mt-4 flex flex-wrap items-center gap-3">
        <button
          type="button"
          disabled={running || !value.trim()}
          onClick={onRun}
          className="inline-flex items-center gap-2 rounded-xl border border-[#ff8b42]/60 bg-[#ff8b42]/20 px-4 py-2 text-sm font-semibold text-white transition hover:bg-[#ff8b42]/35 disabled:cursor-not-allowed disabled:opacity-60"
        >
          <Rocket className="h-4 w-4" />
          Run Workforce
        </button>
        <button
          type="button"
          disabled={running}
          onClick={onDemo}
          className="inline-flex items-center gap-2 rounded-xl border border-[#4aa8ff]/60 bg-[#4aa8ff]/15 px-4 py-2 text-sm font-semibold text-white transition hover:bg-[#4aa8ff]/30 disabled:cursor-not-allowed disabled:opacity-60"
        >
          <PlayCircle className="h-4 w-4" />
          Auto Demo
        </button>
        <span className="mono inline-flex items-center gap-1 text-xs text-[#90a6c6]">
          <Wand2 className="h-3.5 w-3.5" />
          {running ? 'Agents are working...' : 'Ready'}
        </span>
      </div>
    </section>
  );
}
