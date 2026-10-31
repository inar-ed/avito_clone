from sqlalchemy.orm import Session
from app.repositories import user_repo


def create_user(db: Session, name: str, email: str):
    return user_repo.create(db, name, email)
