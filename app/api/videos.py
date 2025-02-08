from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import os
import shutil
from ..dependencies import get_db
from ..models import models, schemas
from ..crud import videos
from ..models.models import VideoStatus
from ..config import settings

router = APIRouter(
    prefix="/videos",
    tags=["videos"]
)

# Constants
ALLOWED_EXTENSIONS = {'.mp4', '.mov', '.avi', '.wmv', '.flv', '.mkv'}

@router.post("/", response_model=schemas.Video)
def create_video(video: schemas.VideoCreate, db: Session = Depends(get_db)):
    # Check if topic exists
    topic = db.query(models.Topic).filter(models.Topic.id == video.topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail=f"Topic with id {video.topic_id} not found")
    return videos.create_video(db=db, video=video)

@router.get("/{video_id}", response_model=schemas.Video)
def get_video(video_id: int, db: Session = Depends(get_db)):
    db_video = videos.get_video(db=db, video_id=video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

@router.get("/", response_model=List[schemas.Video])
def list_videos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return videos.get_videos(db=db, skip=skip, limit=limit)

@router.get("/topic/{topic_id}", response_model=List[schemas.Video])
def get_videos_by_topic(topic_id: int, db: Session = Depends(get_db)):
    return videos.get_videos_by_topic(db=db, topic_id=topic_id)

@router.post("/{video_id}/upload", response_model=schemas.Video)
async def upload_video_file(
    video_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Get existing video record
    db_video = videos.get_video(db=db, video_id=video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    
    # Validate file extension
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    try:
        # Create unique filename
        filename = f"video_{video_id}{file_ext}"
        
        # Use configured upload directory
        file_path = os.path.join(settings.VIDEOS_UPLOAD_DIR, filename)
        
        # Save the file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Update video record with file path and status
        db_video = videos.update_video(
            db=db,
            video_id=video_id,
            video_update={
                "file_path": str(file_path),
                "status": VideoStatus.UPLOADED
            }
        )
        
        return db_video
        
    except Exception as e:
        # Update video status to error if something goes wrong
        videos.update_video_status(
            db=db,
            video_id=video_id,
            status=VideoStatus.ERROR,
            error_message=str(e)
        )
        raise HTTPException(
            status_code=500,
            detail=f"Error uploading file: {str(e)}"
        )

@router.post("/{video_id}/status", response_model=schemas.Video)
def update_status(
    video_id: int,
    status: schemas.VideoStatus,
    error_message: str = None,
    db: Session = Depends(get_db)
):
    db_video = videos.update_video_status(
        db=db,
        video_id=video_id,
        status=status,
        error_message=error_message
    )
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video