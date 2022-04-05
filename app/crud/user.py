from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app import schemas
from app.validator import verify_email_address_exists


def register_user(db: Session, user: schemas.UserCreate):
    existing_user = verify_email_address_exists(user.email, db)
    if existing_user:
        raise HTTPException(status_code=400, detail="User with given email already exists")
    db_user = User(email=user.email, first_name=user.first_name, last_name=user.last_name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
