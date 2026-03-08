# CRUD for User

from db.hash import Hash
from sqlalchemy.orm.session import Session
from db.models import DbUser
from schemas.user import UserBase, UserLogin

# Create a new user
def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Get_all_user
def get_all_users(db: Session):
    return db.query(DbUser).all()

# Get_user_by_id()
def get_user(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()

# Get_user_by_username
def get_user_by_username(db: Session, username:str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username {username} does not exist")
    return user

#update user
def update_user(db: Session, id:int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'


def delete_user(db: Session, id:int):
    user= db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return 'ok'
