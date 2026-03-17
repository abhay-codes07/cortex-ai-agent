import asyncio
from typing import Any

import anyio

from app.realtime import RealtimeEvent, manager


def emit_event(stage: str, message: str, metadata: dict[str, Any] | None = None) -> None:
    event = RealtimeEvent(stage=stage, message=message, metadata=metadata or {})

    try:
        anyio.from_thread.run(manager.broadcast, event)
        return
    except RuntimeError:
        pass

    try:
        loop = asyncio.get_running_loop()
        loop.create_task(manager.broadcast(event))
        return
    except RuntimeError:
        pass

    try:
        asyncio.run(manager.broadcast(event))
    except Exception:
        # Realtime streaming should never break core workflow execution.
        return
