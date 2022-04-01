from sqlalchemy.orm import Session
from app.models.breed import Breed
from app import schemas


def get_breeds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Breed).offset(skip).limit(limit).all()


def get_breeds_by_kind(db: Session, kind_id: int, skip: int = 0, limit: int = 100):
    return db.query(Breed).filter(Breed.kind_id == kind_id).offset(skip).limit(limit).all()


def create_breed(db: Session, breed: schemas.BreedCreate):
    db_breed = Breed(name=breed.name, kind_id=breed.kind_id)
    db.add(db_breed)
    db.commit()
    db.refresh(db_breed)
    return db_breed
