from sqlalchemy.orm import Session
from app.models.alert_type import AlertType
from app import schemas


def get_alert_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AlertType).offset(skip).limit(limit).all()


def create_alert_type(db: Session, alert_type: schemas.AlertTypeCreate):
    alert_type = AlertType(name=alert_type.name)
    db.add(alert_type)
    db.commit()
    db.refresh(alert_type)
    return alert_type
