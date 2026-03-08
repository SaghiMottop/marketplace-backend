# User input/output schemas
from typing import List

from pydantic import BaseModel, ConfigDict

from schemas.ads import AdsBase


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    ads : List[AdsBase] =[]

    class Config:
        from_attributes = True



class UserLogin(BaseModel):
    email: str
    password: str
