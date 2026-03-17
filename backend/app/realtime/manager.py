import asyncio
from collections.abc import Iterable

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

from app.realtime.schemas import RealtimeEvent


class RealtimeConnectionManager:
    def __init__(self) -> None:
        self._connections: set[WebSocket] = set()
        self._lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        async with self._lock:
            self._connections.add(websocket)

    async def disconnect(self, websocket: WebSocket) -> None:
        async with self._lock:
            self._connections.discard(websocket)

    async def broadcast(self, event: RealtimeEvent) -> None:
        stale: list[WebSocket] = []
        async with self._lock:
            for connection in self._connections:
                try:
                    await connection.send_json(event.model_dump(mode='json'))
                except WebSocketDisconnect:
                    stale.append(connection)
                except RuntimeError:
                    stale.append(connection)

            for connection in stale:
                self._connections.discard(connection)

    async def broadcast_many(self, events: Iterable[RealtimeEvent]) -> None:
        for event in events:
            await self.broadcast(event)

    async def stats(self) -> int:
        async with self._lock:
            return len(self._connections)


manager = RealtimeConnectionManager()
