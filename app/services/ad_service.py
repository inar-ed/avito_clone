from sqlalchemy.orm import Session
from app.repositories import ad_repo, user_repo


def create_ad(db: Session, **values):
    if not user_repo.get(db, values["owner_id"]):
        raise ValueError("Owner not found")
    return ad_repo.create(db, **values)
