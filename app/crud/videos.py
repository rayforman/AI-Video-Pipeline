from sqlalchemy.orm import Session
from sqlalchemy.sql import func  # Add this import at the top
from ..models import models, schemas
from typing import List, Optional, Dict, Any

def create_video(db: Session, video: schemas.VideoCreate) -> models.Video:
    db_video = models.Video(
        topic_id=video.topic_id,
        title=video.title,
        description=video.description,
        status=video.status
    )
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def get_video(db: Session, video_id: int) -> Optional[models.Video]:
    return db.query(models.Video).filter(models.Video.id == video_id).first()

def get_videos(db: Session, skip: int = 0, limit: int = 100) -> List[models.Video]:
    return db.query(models.Video).offset(skip).limit(limit).all()

def get_videos_by_topic(db: Session, topic_id: int) -> List[models.Video]:
    return db.query(models.Video).filter(models.Video.topic_id == topic_id).all()

def update_video_status(
    db: Session, 
    video_id: int, 
    status: models.VideoStatus,
    error_message: Optional[str] = None
) -> Optional[models.Video]:
    db_video = get_video(db, video_id)
    if db_video:
        db_video.status = status
        if error_message:
            db_video.error_message = error_message
        db.commit()
        db.refresh(db_video)
    return db_video

def update_video_file(
    db: Session,
    video_id: int,
    file_path: str
) -> Optional[models.Video]:
    db_video = get_video(db, video_id)
    if db_video:
        db_video.file_path = file_path
        db_video.status = models.VideoStatus.UPLOADED
        db.commit()
        db.refresh(db_video)
    return db_video

def update_youtube_data(
    db: Session,
    video_id: int,
    youtube_video_id: str
) -> Optional[models.Video]:
    db_video = get_video(db, video_id)
    if db_video:
        db_video.youtube_video_id = youtube_video_id
        db_video.status = models.VideoStatus.PUBLISHED
        db_video.published_at = func.now()
        db.commit()
        db.refresh(db_video)
    return db_video

# Add this new function along with your existing functions
def update_video(
    db: Session,
    video_id: int,
    video_update: Dict[str, Any]
) -> Optional[models.Video]:
    db_video = get_video(db, video_id)
    if db_video:
        for key, value in video_update.items():
            setattr(db_video, key, value)
        db.commit()
        db.refresh(db_video)
    return db_video