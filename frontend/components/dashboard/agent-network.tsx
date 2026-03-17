"use client";

import { motion } from 'framer-motion';
import { Bot } from 'lucide-react';

type AgentNode = {
  role: string;
  name: string;
  status: 'idle' | 'thinking' | 'working' | 'done' | 'ready';
};

type AgentNetworkProps = {
  nodes: AgentNode[];
};

const statusStyle: Record<AgentNode['status'], string> = {
  idle: 'border-white/20 bg-white/5 text-[#9fb1cc]',
  ready: 'border-[#4aa8ff]/50 bg-[#4aa8ff]/15 text-[#bedfff]',
  thinking: 'border-[#ffb14f]/50 bg-[#ffb14f]/15 text-[#ffd9a8]',
  working: 'border-[#1fd3b4]/50 bg-[#1fd3b4]/15 text-[#b2f6ea]',
  done: 'border-[#5ef57f]/55 bg-[#5ef57f]/15 text-[#d9ffe3]',
};

export function AgentNetwork({ nodes }: AgentNetworkProps) {
  const arranged = nodes.map((node, index) => ({
    ...node,
    top: `${12 + (index % 3) * 31}%`,
    left: `${10 + Math.floor(index / 3) * 44}%`,
  }));

  return (
    <section className="glass-panel relative h-[280px] overflow-hidden rounded-2xl p-5">
      <div className="mb-3 flex items-center justify-between">
        <h2 className="text-lg font-semibold">Agent Network</h2>
        <span className="mono text-xs text-[#95a9c8]">Live Topology</span>
      </div>

      <svg className="absolute inset-0 h-full w-full opacity-40" viewBox="0 0 100 100" preserveAspectRatio="none">
        <line x1="22" y1="20" x2="58" y2="20" stroke="#4aa8ff" strokeWidth="0.4" />
        <line x1="22" y1="20" x2="58" y2="52" stroke="#1fd3b4" strokeWidth="0.4" />
        <line x1="58" y1="20" x2="22" y2="52" stroke="#ff8b42" strokeWidth="0.4" />
        <line x1="58" y1="52" x2="22" y2="84" stroke="#4aa8ff" strokeWidth="0.4" />
        <line x1="22" y1="52" x2="58" y2="84" stroke="#1fd3b4" strokeWidth="0.4" />
      </svg>

      {arranged.map((node, index) => (
        <motion.div
          key={node.role}
          initial={{ opacity: 0, scale: 0.85 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.25, delay: 0.05 * index }}
          className={`absolute w-[42%] rounded-xl border p-3 ${statusStyle[node.status]}`}
          style={{ top: node.top, left: node.left }}
        >
          <div className="flex items-center gap-2">
            <Bot className="h-4 w-4" />
            <p className="text-xs font-semibold uppercase tracking-wider">{node.role}</p>
          </div>
          <p className="mt-1 text-sm font-medium text-white">{node.name}</p>
          <p className="mono mt-1 text-[11px] uppercase tracking-[0.2em]">{node.status}</p>
        </motion.div>
      ))}
    </section>
  );
}
