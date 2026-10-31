from sqlalchemy.orm import Session
from app.models import Category


def create(db: Session, name: str) -> Category:
    category = Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def list_all(db: Session) -> list[Category]:
    return db.query(Category).order_by(Category.name).all()
