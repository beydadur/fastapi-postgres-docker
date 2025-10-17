import datetime as _dt
import pydantic as _pydantic
import typing as _typing

class _ItemBase(_pydantic.BaseModel):
    title: str
    description: str
    price: float

class Item(_ItemBase):
    id: int
    created_at: _dt.datetime

    class Config:
        from_attributes = True

class CreateItem(_ItemBase):
    pass