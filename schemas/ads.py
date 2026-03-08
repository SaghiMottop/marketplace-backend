# Ads input/output schemas
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class AdsBase(BaseModel):
    title: str
    description: str
    price: int
    category_id: int


class AdsDisplay(BaseModel):
    id: int
    title: str
    description: str
    price: int
    category_id: int
    status: str

    class Config:
        from_attributes = True
