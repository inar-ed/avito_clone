from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.ad import AdCreate, AdRead
from app.services.ad_service import create_ad

router = APIRouter()


@router.post("", response_model=AdRead, status_code=201)
def create(payload: AdCreate, db: Session = Depends(get_db)):
    try:
        return create_ad(db, **payload.model_dump())
    except ValueError as exc:
        raise HTTPException(404, str(exc)) from exc
