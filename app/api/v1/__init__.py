from fastapi import APIRouter
from app.api.v1 import users, ads, search, payments, categories, messages

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(ads.router, prefix="/ads", tags=["ads"])
router.include_router(search.router, prefix="/search", tags=["search"])
router.include_router(payments.router, prefix="/payments", tags=["payments"])
router.include_router(categories.router, prefix="/categories", tags=["categories"])
router.include_router(messages.router, prefix="/messages", tags=["messages"])
