from sqlalchemy.orm import Session
from app.models import Message


def create(db: Session, **values) -> Message:
    message = Message(**values)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message
