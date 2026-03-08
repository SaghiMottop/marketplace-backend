# Routes for ads
import token

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status

from auth.oauth2 import oauth2_scheme, get_current_user
from db import  db_ads
from db.database import get_db
from schemas.ads import AdsDisplay, AdsBase
from schemas.user import UserDisplay

router = APIRouter(
    prefix='/ads',
    tags=['ads']
)


@router.post('/', response_model=AdsDisplay, status_code=status.HTTP_201_CREATED)
def create_ads(request: AdsBase, db: Session = Depends(get_db), current_user: UserDisplay=Depends(get_current_user)):
    return db_ads.create_ads(db, request, seller_id=current_user.id)

@router.get('/', response_model=list[AdsDisplay])
def get_all_ads(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db_ads.get_all_ads(db)


@router.get('/{id}')
def get_ads(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    data = db_ads.get_ads(db, id)
    return {
        'data': data,
        'current_user': current_user
    }