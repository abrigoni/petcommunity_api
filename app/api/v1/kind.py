from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, crud, dependencies

router = APIRouter()


@router.get("/", response_model=List[schemas.Kind])
def read_kinds(
        db: Session = Depends(dependencies.get_db),
        skip: int = 0,
        limit: int = 100
):
    """
    Retrieve kinds
    :param db: db dependency
    :param skip: page
    :param limit: items per page
    :return: kinds
    """
    return crud.get_kinds(db, skip, limit)


@router.post("/", response_model=schemas.Kind)
def create_kind(
        kind: schemas.KindCreate,
        db: Session = Depends(dependencies.get_db),
):
    return crud.create_kind(db, kind)
