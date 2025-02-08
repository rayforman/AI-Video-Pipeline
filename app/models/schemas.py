from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from ..models.models import ContentStatus, VideoStatus  # Add VideoStatus to imports

class TopicBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: ContentStatus = ContentStatus.PENDING

class TopicCreate(TopicBase):
    pass

class Topic(TopicBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class VideoBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: VideoStatus = VideoStatus.PENDING

class VideoCreate(VideoBase):
    topic_id: int

class Video(VideoBase):
    id: int
    topic_id: int
    file_path: Optional[str] = None
    youtube_video_id: Optional[str] = None
    error_message: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    published_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)