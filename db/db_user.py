from sqlalchemy.orm import Session

from db.hash import Hash
from db.models import DBUser
from schemas.user import UserBase


def create_user(db:Session, request: UserBase):
    new_user = DBUser(
        username = request.username,
        email = request.email,
        password = Hash(request.password)
    )
