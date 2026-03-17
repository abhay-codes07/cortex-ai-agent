from redis.exceptions import RedisError
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import SessionLocal
from app.services.cache_service import CacheService


class SystemService:
    def db_status(self) -> str:
        try:
            db = SessionLocal()
            db.execute(text('SELECT 1'))
            db.close()
            return 'ok'
        except SQLAlchemyError:
            return 'degraded'

    def redis_status(self) -> str:
        cache = CacheService()
        try:
            cache.set_json('system:ping', {'ok': True}, ttl=5)
            return 'ok' if cache.get_json('system:ping') else 'degraded'
        except RedisError:
            return 'degraded'

    def overall_status(self) -> dict[str, str]:
        db = self.db_status()
        redis = self.redis_status()
        overall = 'ok' if db == 'ok' and redis == 'ok' else 'degraded'
        return {'overall': overall, 'database': db, 'redis': redis}
