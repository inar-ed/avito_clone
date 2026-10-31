from datetime import datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class PaymentCreate(BaseModel):
    ad_id: int
    buyer_id: int
    currency: str = Field(default="RUB", min_length=3, max_length=3)


class PaymentStatusUpdate(BaseModel):
    status: Literal["succeeded", "failed", "cancelled"]


class PaymentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    ad_id: int
    buyer_id: int
    amount: Decimal
    currency: str
    status: str
    created_at: datetime
