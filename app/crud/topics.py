from sqlalchemy.orm import Session
from ..models import models, schemas

def create_topic(db: Session, topic: schemas.TopicCreate) -> models.Topic:
    db_topic = models.Topic(
        title=topic.title,
        description=topic.description,
        status=topic.status
    )
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic