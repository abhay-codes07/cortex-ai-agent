"use client";

export default function DashboardError({ reset }: { error: Error; reset: () => void }) {
  return (
    <main className="cortex-grid min-h-screen px-4 py-6 md:px-10 md:py-8">
      <section className="mx-auto w-full max-w-3xl">
        <div className="glass-panel rounded-2xl p-6">
          <p className="text-lg font-semibold">Dashboard hit an unexpected error.</p>
          <p className="mt-2 text-sm text-[#aac0dc]">Use reset to recover instantly for demo continuity.</p>
          <button
            type="button"
            onClick={reset}
            className="mt-4 rounded-lg border border-[#4aa8ff]/55 bg-[#4aa8ff]/20 px-4 py-2 text-sm font-semibold"
          >
            Reset Dashboard
          </button>
        </div>
      </section>
    </main>
  );
}
