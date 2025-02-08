from sqlalchemy import Column, Integer, String, DateTime, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from ..database import Base

class ContentStatus(str, enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

class VideoStatus(str, enum.Enum):
    PENDING = "PENDING"           # Initial state when video is first created
    UPLOADED = "UPLOADED"         # MP4 has been uploaded to our system
    PROCESSING = "PROCESSING"     # Being processed for YouTube
    PUBLISHED = "PUBLISHED"       # Successfully uploaded to YouTube
    FAILED = "FAILED"            # Upload or processing failed

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(ContentStatus), default=ContentStatus.PENDING, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Add this line inside the Topic class
    videos = relationship("Video", back_populates="topic")

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    file_path = Column(String(255), nullable=True)  # Path to the uploaded MP4 file
    youtube_video_id = Column(String(50), nullable=True)  # ID of the uploaded YouTube video
    status = Column(Enum(VideoStatus), default=VideoStatus.PENDING, nullable=False)
    error_message = Column(Text, nullable=True)  # For storing error details if something fails
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    published_at = Column(DateTime(timezone=True), nullable=True)  # When the video was published to YouTube
    
    # Relationship to Topic
    topic = relationship("Topic", back_populates="videos")