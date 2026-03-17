"use client";

type MetricChipProps = {
  label: string;
  value: string;
  tone: 'mint' | 'sky' | 'amber';
};

const toneClass = {
  mint: 'border-[#1fd3b4]/45 bg-[#1fd3b4]/15 text-[#b2f6ea]',
  sky: 'border-[#4aa8ff]/45 bg-[#4aa8ff]/15 text-[#cae4ff]',
  amber: 'border-[#ff8b42]/45 bg-[#ff8b42]/15 text-[#ffd4b8]',
};

export function MetricChip({ label, value, tone }: MetricChipProps) {
  return (
    <span className={`inline-flex items-center gap-2 rounded-lg border px-3 py-1.5 text-sm ${toneClass[tone]}`}>
      <span className="mono text-[10px] uppercase tracking-[0.2em]">{label}</span>
      <span className="font-semibold text-white">{value}</span>
    </span>
  );
}
