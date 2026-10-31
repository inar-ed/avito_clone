from sqlalchemy.orm import Session
from app.models import Payment


def create(db: Session, **values) -> Payment:
    payment = Payment(**values)
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment


def get(db: Session, payment_id: int) -> Payment | None:
    return db.get(Payment, payment_id)


def list_for_buyer(db: Session, buyer_id: int) -> list[Payment]:
    return db.query(Payment).filter(Payment.buyer_id == buyer_id).order_by(Payment.id.desc()).all()
