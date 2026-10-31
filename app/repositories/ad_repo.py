from sqlalchemy.orm import Session
from app.models import Ad


def create(db: Session, **values) -> Ad:
    ad = Ad(**values)
    db.add(ad)
    db.commit()
    db.refresh(ad)
    return ad


def get(db: Session, ad_id: int) -> Ad | None:
    return db.get(Ad, ad_id)


def search(db: Session, query: str = "") -> list[Ad]:
    return db.query(Ad).filter(Ad.title.ilike(f"%{query}%")).all()
