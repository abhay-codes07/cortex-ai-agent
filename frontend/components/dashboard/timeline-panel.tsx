"use client";

import type { TimelineEvent } from '@/lib/types';

type TimelinePanelProps = {
  events: TimelineEvent[];
};

export function TimelinePanel({ events }: TimelinePanelProps) {
  return (
    <section className="glass-panel rounded-2xl p-5">
      <div className="mb-4 flex items-center justify-between">
        <h2 className="text-lg font-semibold">Execution Timeline</h2>
        <span className="mono text-xs text-[#8ea3c3]">chronological</span>
      </div>
      <div className="space-y-3">
        {events.length === 0 ? <p className="text-sm text-[#90a5c5]">No timeline yet. Run a mission to populate this panel.</p> : null}
        {events.map((event, index) => (
          <div key={`${event.stage}-${index}`} className="relative rounded-xl border border-white/12 bg-white/5 p-3 pl-5">
            <span className="absolute left-2 top-4 h-2 w-2 rounded-full bg-[#1fd3b4]" />
            <p className="mono text-[11px] uppercase tracking-[0.2em] text-[#93a8c8]">{event.stage}</p>
            <p className="mt-1 text-sm text-white/90">{event.message}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
