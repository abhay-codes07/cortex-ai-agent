import type { TimelineEvent } from './types';

export type RealtimeConnectionState = 'connecting' | 'connected' | 'disconnected';

export type RealtimeHandlers = {
  onEvent: (event: TimelineEvent) => void;
  onStateChange: (state: RealtimeConnectionState) => void;
};

function toWebSocketUrl(baseUrl: string): string {
  const normalized = baseUrl.replace(/\/$/, '');
  if (normalized.startsWith('https://')) return normalized.replace('https://', 'wss://');
  if (normalized.startsWith('http://')) return normalized.replace('http://', 'ws://');
  return `ws://${normalized}`;
}

export function connectRealtime(handlers: RealtimeHandlers): WebSocket {
  const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://localhost:8000';
  const socketUrl = `${toWebSocketUrl(baseUrl)}/api/v1/realtime/ws`;

  const socket = new WebSocket(socketUrl);
  handlers.onStateChange('connecting');

  socket.onopen = () => {
    handlers.onStateChange('connected');
  };

  socket.onclose = () => {
    handlers.onStateChange('disconnected');
  };

  socket.onerror = () => {
    handlers.onStateChange('disconnected');
  };

  socket.onmessage = (event) => {
    try {
      const payload = JSON.parse(event.data) as TimelineEvent & { type?: string };
      if (payload.type === 'pong') return;
      handlers.onEvent(payload);
    } catch {
      // Ignore invalid websocket payloads to keep demo resilient.
    }
  };

  return socket;
}
