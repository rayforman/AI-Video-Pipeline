from pydantic_settings import BaseSettings

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
    
    class Config:
        env_file = ".env"

settings = Settings()