from sqlalchemy.orm import Session
from app.models import User


def create(db: Session, name: str, email: str) -> User:
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)
