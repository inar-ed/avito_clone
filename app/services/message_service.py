from sqlalchemy.orm import Session
from app.models import Message
from app.repositories import message_repo, user_repo, ad_repo


def create_message(db: Session, **values) -> Message:
    if user_repo.get(db, values["sender_id"]) is None:
        raise ValueError("Sender not found")
    if user_repo.get(db, values["recipient_id"]) is None:
        raise ValueError("Recipient not found")
    if values.get("ad_id") is not None and ad_repo.get(db, values["ad_id"]) is None:
        raise ValueError("Ad not found")
    return message_repo.create(db, **values)
