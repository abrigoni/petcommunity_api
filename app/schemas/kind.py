from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class KindBase(BaseModel):
    name: str


class KindCreate(KindBase):
    pass


class KindUpdate(KindBase):
    pass


class Kind(KindBase):
    id: int
    name: str
    deleted: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


