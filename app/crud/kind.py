from sqlalchemy.orm import Session
from app.models.kind import Kind
from app import schemas


def get_kinds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Kind).offset(skip).limit(limit).all()


def create_kind(db: Session, kind: schemas.KindCreate):
    db_kind = Kind(name=kind.name)
    db.add(db_kind)
    db.commit()
    db.refresh(db_kind)
    return db_kind
