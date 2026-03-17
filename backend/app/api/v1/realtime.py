from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status

from app.realtime import RealtimeStatus, manager
from app.services.realtime_service import emit_event

router = APIRouter(prefix='/realtime')


@router.get('/status', response_model=RealtimeStatus, status_code=status.HTTP_200_OK)
async def realtime_status() -> RealtimeStatus:
    count = await manager.stats()
    return RealtimeStatus(connections=count)


@router.websocket('/ws')
async def realtime_ws(websocket: WebSocket) -> None:
    await manager.connect(websocket)
    emit_event('system', 'Realtime client connected')

    try:
        while True:
            payload = await websocket.receive_text()
            if payload.strip().lower() == 'ping':
                await websocket.send_json({'type': 'pong'})
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        emit_event('system', 'Realtime client disconnected')
