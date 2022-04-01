from pydantic import BaseModel


class AlertTypeBase(BaseModel):
    name: str


class AlertTypeCreate(AlertTypeBase):
    pass


class AlertTypeUpdate(AlertTypeBase):
    pass


class AlertType(AlertTypeBase):
    id: int
    name: str

    class Config:
        orm_mode = True
