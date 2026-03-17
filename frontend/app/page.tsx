"use client";

import Link from 'next/link';
import { motion } from 'framer-motion';
import { ArrowRight, Bot, Orbit, Sparkles } from 'lucide-react';

const cards = [
  {
    icon: Orbit,
    title: 'Autonomous Collaboration',
    description: 'Specialized agents coordinate as a workforce, not a chat response.',
  },
  {
    icon: Bot,
    title: 'Visible Intelligence',
    description: 'Reasoning, actions, tool calls, and progress stream in front of you.',
  },
  {
    icon: Sparkles,
    title: 'Demo-Ready Reliability',
    description: 'One-click demo mode delivers an always-impressive live run.',
  },
];

export default function HomePage() {
  return (
    <main className="cortex-grid min-h-screen px-6 py-10 md:px-12">
      <section className="mx-auto flex w-full max-w-6xl flex-col gap-8">
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.45 }}
          className="glass-panel rounded-3xl p-8 md:p-12"
        >
          <p className="mb-5 inline-flex rounded-full border border-white/20 bg-white/10 px-4 py-1 text-xs uppercase tracking-[0.24em] text-[#ffd4b8]">
            Cortex // Autonomous AI Workforce
          </p>
          <h1 className="max-w-4xl text-4xl font-bold leading-tight md:text-6xl">
            Your AI Workforce That Actually Works
          </h1>
          <p className="mt-5 max-w-2xl text-lg text-[#c4d0e2]">
            Give one objective. Watch multiple AI agents break it down, collaborate, execute tools, and deliver outcomes in real time.
          </p>
          <div className="mt-8 flex flex-wrap items-center gap-4">
            <Link
              href="/dashboard"
              className="inline-flex items-center gap-2 rounded-xl border border-[#ff8b42]/60 bg-[#ff8b42]/20 px-5 py-3 text-sm font-semibold text-white transition hover:bg-[#ff8b42]/35"
            >
              Launch Dashboard
              <ArrowRight className="h-4 w-4" />
            </Link>
            <span className="mono text-sm text-[#9fb0ca]">Phase 8: Premium Frontend UX</span>
          </div>
        </motion.div>

        <div className="grid gap-4 md:grid-cols-3">
          {cards.map((card, index) => {
            const Icon = card.icon;
            return (
              <motion.article
                key={card.title}
                initial={{ opacity: 0, y: 14 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.35, delay: index * 0.1 }}
                className="glass-panel rounded-2xl p-5"
              >
                <Icon className="mb-3 h-7 w-7 text-[#1fd3b4]" />
                <h2 className="text-xl font-semibold">{card.title}</h2>
                <p className="mt-2 text-[#c4d0e2]">{card.description}</p>
              </motion.article>
            );
          })}
        </div>
      </section>
    </main>
  );
}
