from pydantic import BaseModel
from .kind import Kind


class BreedBase(BaseModel):
    name: str = None
    kind_id: int = None


class BreedCreate(BreedBase):
    pass


class BreedUpdate(BreedBase):
    pass


class Breed(BreedBase):
    id: int
    name: str
    kind_id: int
    kind: Kind

    class Config:
        orm_mode = True
