from pydantic_settings import BaseSettings
import os
from pathlib import Path

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    
    # OpenAI
    OPENAI_API_KEY: str
    
    # Fliki
    FLIKI_API_KEY: str
    
    # YouTube
    YOUTUBE_CLIENT_ID: str
    YOUTUBE_CLIENT_SECRET: str
    YOUTUBE_REFRESH_TOKEN: str
    
    # App Settings
    ENVIRONMENT: str = "development"
    MAX_VIDEOS_PER_DAY: int = 10
    
    # Upload Settings
    UPLOAD_DIR: str = "uploads"
    MAX_FILE_SIZE: int = 500 * 1024 * 1024  # 500MB
    
    @property
    def VIDEOS_UPLOAD_DIR(self) -> Path:
        video_dir = Path(self.UPLOAD_DIR) / "videos"
        video_dir.mkdir(parents=True, exist_ok=True)
        return video_dir
    
    class Config:
        env_file = ".env"

settings = Settings()