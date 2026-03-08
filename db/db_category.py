from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db.models import DbCategory


def create_category(db: Session, request):
    existing_category = db.query(DbCategory).filter(DbCategory.name == request.name).first()
    if existing_category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category already exists"
        )

    new_category = DbCategory(name=request.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
