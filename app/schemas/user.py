from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str


class UserCreate(UserBase):
    email: str
    password: str


class UserUpdate(UserBase):
    password: str


class User(UserBase):
    id: int
    email: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
