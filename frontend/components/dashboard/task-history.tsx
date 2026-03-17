"use client";

type HistoryItem = {
  id: string;
  title: string;
  status: string;
  created_at: string;
};

type TaskHistoryProps = {
  items: HistoryItem[];
};

export function TaskHistory({ items }: TaskHistoryProps) {
  return (
    <section className="glass-panel rounded-2xl p-5">
      <div className="mb-4 flex items-center justify-between">
        <h2 className="text-lg font-semibold">Task History</h2>
        <span className="mono text-xs text-[#90a5c5]">recent runs</span>
      </div>
      <div className="space-y-3">
        {items.length === 0 ? <p className="text-sm text-[#90a5c5]">No completed tasks yet.</p> : null}
        {items.map((item) => (
          <article key={item.id} className="rounded-xl border border-white/12 bg-white/5 p-3">
            <p className="text-sm font-medium text-white">{item.title}</p>
            <div className="mt-2 flex items-center justify-between text-xs text-[#9eb0ca]">
              <span className="mono uppercase tracking-wider">{item.status}</span>
              <span>{new Date(item.created_at).toLocaleString()}</span>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
