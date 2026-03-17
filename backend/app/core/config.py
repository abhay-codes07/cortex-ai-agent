from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    app_env: str = Field(default='development', alias='APP_ENV')
    app_name: str = Field(default='Cortex API', alias='APP_NAME')
    app_version: str = Field(default='0.2.0', alias='APP_VERSION')

    cors_origins_raw: str = Field(default='http://localhost:3000', alias='CORS_ORIGINS')

    database_url: str = Field(
        default='postgresql+psycopg://cortex:cortex@localhost:5432/cortex', alias='DATABASE_URL'
    )
    redis_url: str = Field(default='redis://localhost:6379/0', alias='REDIS_URL')
    redis_ttl_seconds: int = Field(default=120, alias='REDIS_TTL_SECONDS')

    api_v1_prefix: str = Field(default='/api/v1', alias='API_V1_PREFIX')

    @property
    def cors_origins(self) -> List[str]:
        return [origin.strip() for origin in self.cors_origins_raw.split(',') if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
