from sqlalchemy import Column, Integer, String
from app.db.session import Base


class AlertType(Base):
    __tablename__ = 'alert_types'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
