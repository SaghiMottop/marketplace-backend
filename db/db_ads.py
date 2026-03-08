# CRUD for Ads

from sqlalchemy.orm.session import Session

from db.models import DbAds
from schemas.ads import AdsBase


def create_ads(db: Session, request: AdsBase, seller_id: int):
    new_ad = DbAds(
        title=request.title,
        description=request.description,
        price=request.price,
        category_id=request.category_id,
        seller_id=seller_id,

    )
    db.add(new_ad)
    db.commit()
    db.refresh(new_ad)
    return new_ad


def get_all_ads(db: Session):
    return db.query(DbAds).all()


def get_ads(db: Session, id: int):
    return db.query(DbAds).filter(DbAds.id == id).first()


