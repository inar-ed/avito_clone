from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.payment_repo import get, list_for_buyer
from app.schemas.payment import PaymentCreate, PaymentRead, PaymentStatusUpdate
from app.services.payment_service import create_payment, update_payment_status

router = APIRouter()


@router.post("", response_model=PaymentRead, status_code=status.HTTP_201_CREATED)
def start_payment(payload: PaymentCreate, db: Session = Depends(get_db)):
    try:
        return create_payment(db, **payload.model_dump())
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.get("/buyer/{buyer_id}", response_model=list[PaymentRead])
def buyer_payments(buyer_id: int, db: Session = Depends(get_db)):
    return list_for_buyer(db, buyer_id)


@router.get("/{payment_id}", response_model=PaymentRead)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = get(db, payment_id)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment


@router.patch("/{payment_id}/status", response_model=PaymentRead)
def finish_payment(payment_id: int, payload: PaymentStatusUpdate, db: Session = Depends(get_db)):
    try:
        return update_payment_status(db, payment_id, payload.status)
    except ValueError as exc:
        raise HTTPException(status_code=404 if str(exc) == "Payment not found" else 409,
                            detail=str(exc)) from exc
