from sqlalchemy.orm import Session
from app.models import Payment
from app.repositories import ad_repo, payment_repo, user_repo


def create_payment(db: Session, ad_id: int, buyer_id: int, currency: str = "RUB") -> Payment:
    ad = ad_repo.get(db, ad_id)
    if ad is None:
        raise ValueError("Ad not found")
    if user_repo.get(db, buyer_id) is None:
        raise ValueError("Buyer not found")
    if ad.owner_id == buyer_id:
        raise ValueError("An owner cannot buy their own ad")
    if db.query(Payment).filter(Payment.ad_id == ad_id, Payment.status == "succeeded").first():
        raise ValueError("Ad has already been paid for")
    return payment_repo.create(db, ad_id=ad_id, buyer_id=buyer_id, amount=ad.price,
                               currency=currency.upper(), status="pending")


def update_payment_status(db: Session, payment_id: int, status: str) -> Payment:
    payment = payment_repo.get(db, payment_id)
    if payment is None:
        raise ValueError("Payment not found")
    if payment.status != "pending":
        raise ValueError("Only pending payments can be finalized")
    payment.status = status
    db.commit()
    db.refresh(payment)
    return payment
