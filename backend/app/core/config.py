from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    app_env: str = Field(default='development', alias='APP_ENV')
    app_name: str = Field(default='Cortex API', alias='APP_NAME')
    cors_origins_raw: str = Field(default='http://localhost:3000', alias='CORS_ORIGINS')

    @property
    def cors_origins(self) -> List[str]:
        return [origin.strip() for origin in self.cors_origins_raw.split(',') if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
