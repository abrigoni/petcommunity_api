from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, crud, dependencies

router = APIRouter()


@router.get("/", response_model=List[schemas.Breed])
def read_breeds(
        db: Session = Depends(dependencies.get_db),
        skip: int = 0,
        limit: int = 100
):
    """
    Retrieve breeds
    :param db: db dependency
    :param skip: page
    :param limit: items per page
    :return: breeds
    """
    return crud.get_breeds(db, skip, limit)


@router.get("/by-kind/{kind_id}", response_model=List[schemas.Breed])
def read_breeds_by_kind(
        kind_id: int,
        db: Session = Depends(dependencies.get_db),
        skip: int = 0,
        limit: int = 100
):
    """
    Retrieve breeds by kind id
    :param kind_id kind primary key to filter breeds
    :param db: db dependency
    :param skip: page
    :param limit: items per page
    :return: breeds
    """
    return crud.get_breeds_by_kind(db, kind_id, skip, limit)


@router.post("/", response_model=schemas.Breed)
def create_breed(
        breed: schemas.BreedCreate,
        db: Session = Depends(dependencies.get_db),
):
    return crud.create_breed(db, breed)
