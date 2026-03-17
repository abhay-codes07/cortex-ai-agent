"use client";

import { TerminalSquare } from 'lucide-react';

type LogStreamProps = {
  logs: string[];
};

export function LogStream({ logs }: LogStreamProps) {
  return (
    <section className="glass-panel flex h-[280px] flex-col rounded-2xl p-5">
      <div className="mb-3 flex items-center justify-between">
        <h2 className="inline-flex items-center gap-2 text-lg font-semibold">
          <TerminalSquare className="h-5 w-5 text-[#1fd3b4]" />
          Live Logs
        </h2>
        <span className="mono text-xs text-[#8ea3c3]">stream</span>
      </div>
      <div className="mono flex-1 space-y-2 overflow-y-auto rounded-xl border border-white/10 bg-black/25 p-3 text-xs text-[#d5e4ff]">
        {logs.length === 0 ? <p className="text-[#8398b8]">Awaiting mission execution...</p> : null}
        {logs.map((log, index) => (
          <p key={`${log}-${index}`} className="leading-relaxed">
            {log}
          </p>
        ))}
      </div>
    </section>
  );
}
