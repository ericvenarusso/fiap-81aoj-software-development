from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str
    app_version: str
    app_description: str
    mongodb_url: str
    model_path: str

    class Config:
        env_file = "config/api/dev.env"
        
@lru_cache
def get_settings():
    """
        Include the settings on cache usin lru algorithm.
    """
    return Settings()
