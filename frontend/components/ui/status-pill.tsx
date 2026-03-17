interface StatusPillProps {
  label: string;
}

export function StatusPill({ label }: StatusPillProps) {
  return (
    <span className="inline-flex items-center rounded-full border border-white/20 bg-white/10 px-3 py-1 text-xs font-medium uppercase tracking-wider text-white/90">
      {label}
    </span>
  );
}
