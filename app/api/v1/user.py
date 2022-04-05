from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, crud, dependencies

router = APIRouter()


@router.post("/", response_model=schemas.User)
def register_user(
        user: schemas.UserCreate,
        db: Session = Depends(dependencies.get_db),
):
    return crud.register_user(db, user)
