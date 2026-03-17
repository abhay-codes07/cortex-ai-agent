"use client";

import type { MemoryRecallItem } from '@/lib/types';

type MemoryPanelProps = {
  items: MemoryRecallItem[];
};

export function MemoryPanel({ items }: MemoryPanelProps) {
  return (
    <section className="glass-panel rounded-2xl p-5">
      <div className="mb-4 flex items-center justify-between">
        <h2 className="text-lg font-semibold">Memory Recall</h2>
        <span className="mono text-xs text-[#90a5c5]">long-term</span>
      </div>
      <div className="space-y-3">
        {items.length === 0 ? <p className="text-sm text-[#90a5c5]">No memory signals for current objective.</p> : null}
        {items.map((item, index) => (
          <article key={`${item.summary}-${index}`} className="rounded-xl border border-white/12 bg-white/5 p-3">
            <p className="text-sm text-white/90">{item.summary}</p>
            <div className="mt-2 flex items-center justify-between text-xs text-[#a7b9d1]">
              <span className="mono uppercase tracking-wider">{item.workflow_mode}</span>
              <span>score: {(item.relevance_score ?? 0).toFixed(2)}</span>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
