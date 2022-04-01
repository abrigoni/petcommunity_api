from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from app.db.session import Base


class Kind(Base):
    __tablename__ = "kinds"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    deleted = Column(Boolean, nullable=True)
    created_at = Column(Date, nullable=True)
    updated_at = Column(Date, nullable=True)
    deleted_at = Column(Date, nullable=True)
    breeds = relationship("Breed")
