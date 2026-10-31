from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class AdCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = ""
    price: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    owner_id: int
    category_id: int | None = None


class AdRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str
    price: Decimal
    owner_id: int
    category_id: int | None
