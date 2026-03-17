export default function DashboardLoading() {
  return (
    <main className="cortex-grid min-h-screen px-4 py-6 md:px-10 md:py-8">
      <section className="mx-auto w-full max-w-[1400px]">
        <div className="glass-panel animate-pulse rounded-2xl p-6">
          <p className="mono text-xs text-[#8ea3c3]">Booting Cortex dashboard...</p>
          <div className="mt-4 h-4 w-2/3 rounded bg-white/10" />
          <div className="mt-2 h-4 w-1/2 rounded bg-white/10" />
        </div>
      </section>
    </main>
  );
}
