from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base
from .kind import Kind


class Breed(Base):
    __tablename__ = 'breeds'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    kind_id = Column(Integer, ForeignKey('kinds.id'))
    kind = relationship('Kind', primaryjoin=kind_id == Kind.id)
