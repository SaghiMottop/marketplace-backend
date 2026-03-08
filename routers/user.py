# Routes for user actions (register, login, update)
from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db import db_user
from db.database import get_db

from schemas.user import UserBase, UserDisplay

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# creat user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db_user.get_all_users(db)

@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db_user.get_user(db, id)


@router.put('/{id}/update')
def update_user(id: int, request: UserBase, db: Session= Depends(get_db), current_user = Depends(get_current_user)):
    return db_user.update_user(db, id, request)

@router.delete('/delete/{id}')
def delete_user(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db_user.delete_user(db, id)