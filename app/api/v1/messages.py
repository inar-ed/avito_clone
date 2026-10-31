from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.message import MessageCreate, MessageRead
from app.services.message_service import create_message

router = APIRouter()


@router.post("", response_model=MessageRead, status_code=201)
def send_message(payload: MessageCreate, db: Session = Depends(get_db)):
    try:
        return create_message(db, **payload.model_dump())
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
