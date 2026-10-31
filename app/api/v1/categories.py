from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.category_repo import create, list_all
from app.schemas.category import CategoryCreate, CategoryRead

router = APIRouter()


@router.get("", response_model=list[CategoryRead])
def categories(db: Session = Depends(get_db)):
    return list_all(db)


@router.post("", response_model=CategoryRead, status_code=201)
def add_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    try:
        return create(db, payload.name)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=409, detail="Category already exists") from exc
