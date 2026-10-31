from sqlalchemy.orm import Session
from app.repositories.ad_repo import search


def search_ads(db: Session, query: str = ""):
    return search(db, query)
