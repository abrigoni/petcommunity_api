from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, crud, dependencies

router = APIRouter()


@router.get("/", response_model=List[schemas.AlertType])
def read_alert_types(
        db: Session = Depends(dependencies.get_db),
        skip: int = 0,
        limit: int = 100
):
    """
    Retrieve Alert Types
    :param db: db dependency
    :param skip: page
    :param limit: items per page
    :return: alert_types
    """
    return crud.get_alert_types(db, skip, limit)


@router.post("/", response_model=schemas.AlertType)
def create_alert_type(
        alert_type: schemas.AlertTypeCreate,
        db: Session = Depends(dependencies.get_db),
):
    return crud.create_alert_type(db, alert_type)
