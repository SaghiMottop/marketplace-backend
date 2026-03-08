# Routes for category
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db import db_ads, db_category
from db.database import get_db
from schemas.ads import AdsDisplay, AdsBase
from schemas.category import CategoryDisplay, CategoryBase

router = APIRouter(
    prefix='/category',
    tags=['category']
)


@router.post('/', response_model=CategoryDisplay)
def create_category(request: CategoryBase, db: Session= Depends(get_db), current_user = Depends(get_current_user)):
    return db_category.create_category(db, request)