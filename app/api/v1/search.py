from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.ad import AdRead
from app.services.search_service import search_ads

router = APIRouter()


@router.get("", response_model=list[AdRead])
def search(q: str = Query(default=""), db: Session = Depends(get_db)):
    return search_ads(db, q)
