from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Dict

from ..models import schemas
from ..models.models import ContentStatus
from ..dependencies import get_db
from ..services.openai_service import generate_video_topic
from ..crud import topics as topics_crud

router = APIRouter(
    prefix="/topics",
    tags=["topics"]
)

@router.post("/generate", response_model=schemas.Topic)
def generate_topic(db: Session = Depends(get_db)):
    try:
        # Generate topic using OpenAI
        topic_data = generate_video_topic()
        
        # Create topic object
        topic_create = schemas.TopicCreate(
            title=topic_data["title"],
            description=topic_data["description"],
            status=ContentStatus.PENDING
        )
        
        # Save to database
        db_topic = topics_crud.create_topic(db=db, topic=topic_create)
        
        return db_topic
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate topic: {str(e)}"
        )

@router.post("/", response_model=schemas.Topic)
def create_topic(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
    return topics_crud.create_topic(db=db, topic=topic)