from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import create_user
from app.repositories.user_repo import get

router = APIRouter()


@router.post("", response_model=UserRead, status_code=201)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, payload.name, payload.email)


@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get(db, user_id)
    if user is None:
        raise HTTPException(404, "User not found")
    return user
