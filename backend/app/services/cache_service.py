import json
from typing import Any

import redis
from redis.exceptions import RedisError

from app.core.config import settings


class CacheService:
    def __init__(self) -> None:
        self._client: redis.Redis | None = None

    def _client_or_none(self) -> redis.Redis | None:
        if self._client is None:
            try:
                self._client = redis.Redis.from_url(settings.redis_url, decode_responses=True)
                self._client.ping()
            except RedisError:
                self._client = None
        return self._client

    def get_json(self, key: str) -> dict[str, Any] | None:
        client = self._client_or_none()
        if not client:
            return None

        payload = client.get(key)
        if not payload:
            return None

        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            return None

    def set_json(self, key: str, value: dict[str, Any], ttl: int | None = None) -> None:
        client = self._client_or_none()
        if not client:
            return

        expiration = ttl if ttl is not None else settings.redis_ttl_seconds
        client.setex(key, expiration, json.dumps(value, default=str))

    def invalidate(self, key: str) -> None:
        client = self._client_or_none()
        if not client:
            return
        client.delete(key)
