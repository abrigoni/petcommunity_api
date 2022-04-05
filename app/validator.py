from sqlalchemy.orm import Session
from app.models.user import User
from typing import Optional


def verify_email_address_exists(email: str, db_session: Session) -> Optional[User]:
    return db_session.query(User).filter(User.email == email).first()
