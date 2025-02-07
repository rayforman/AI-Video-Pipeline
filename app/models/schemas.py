from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from ..models.models import ContentStatus

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