"use client";

import { motion } from 'framer-motion';
import { Sparkles, Workflow, ShieldCheck } from 'lucide-react';

const cards = [
  {
    icon: Workflow,
    title: 'Multi-Agent Collaboration',
    description: 'Coordinated AI agents break down goals and execute tasks together.'
  },
  {
    icon: Sparkles,
    title: 'Live Intelligence',
    description: 'Watch reasoning, tool calls, and task execution stream in real-time.'
  },
  {
    icon: ShieldCheck,
    title: 'Production-Ready',
    description: 'Built with FastAPI, PostgreSQL, Redis, and a polished Next.js UI.'
  }
];

export default function HomePage() {
  return (
    <main className="min-h-screen px-6 py-12 md:px-12">
      <section className="mx-auto flex max-w-6xl flex-col gap-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="rounded-3xl border border-white/15 bg-white/10 p-10 backdrop-blur-xl"
        >
          <p className="mb-5 inline-block rounded-full border border-ember/40 bg-ember/15 px-4 py-1 text-sm font-medium text-ember">
            Cortex - Phase 1 Initialized
          </p>
          <h1 className="max-w-3xl text-4xl font-bold tracking-tight md:text-6xl">
            Your AI Workforce That Actually Works
          </h1>
          <p className="mt-6 max-w-2xl text-lg text-white/80">
            Cortex transforms one high-level task into coordinated action across specialized agents.
            This is the foundation for an autonomous AI workforce experience.
          </p>
        </motion.div>

        <div className="grid gap-5 md:grid-cols-3">
          {cards.map((card, index) => {
            const Icon = card.icon;
            return (
              <motion.article
                key={card.title}
                initial={{ opacity: 0, y: 24 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.45, delay: 0.15 * index }}
                className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur"
              >
                <Icon className="mb-4 h-8 w-8 text-aurora" />
                <h2 className="text-xl font-semibold">{card.title}</h2>
                <p className="mt-3 text-white/75">{card.description}</p>
              </motion.article>
            );
          })}
        </div>
      </section>
    </main>
  );
}
