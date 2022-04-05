from sqlalchemy import Column, Integer, String, Date, func
from app.db.session import Base
from app import hashing


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), nullable=False, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(Date, nullable=True, server_default=func.now())
    updated_at = Column(Date, nullable=True, onupdate=func.now())

    def __init__(self, email: str, first_name:str, last_name: str, password: str):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = hashing.get_password_hash(password)

    def check_password(self, password: str) -> bool:
        return hashing.verify_password(password, self.password)
