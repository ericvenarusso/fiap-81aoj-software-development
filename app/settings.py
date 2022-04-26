from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str
    app_version: str
    app_description: str
    model_path: str

    class Config:
        env_file = "dev.env"
        
@lru_cache
def get_settings():
    """
        Include the settings on cache usin lru algorithm.
    """
    return Settings()
