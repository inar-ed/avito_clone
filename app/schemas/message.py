from pydantic import BaseModel, ConfigDict, Field


class MessageCreate(BaseModel):
    sender_id: int
    recipient_id: int
    ad_id: int | None = None
    body: str = Field(min_length=1)


class MessageRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    sender_id: int
    recipient_id: int
    ad_id: int | None
    body: str
