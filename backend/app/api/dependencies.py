from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.cache_service import CacheService


def get_db_session() -> Session:
    yield from get_db()


def get_cache_service() -> CacheService:
    return CacheService()
