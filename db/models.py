
from sqlalchemy.sql.sqltypes import Integer, String, Text, DateTime
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint
from sqlalchemy import Column, Enum as SAEnum, text,Boolean
from sqlalchemy.sql.functions import func
from sqlalchemy.orm import relationship
from db.database import Base
import enum




class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    ads = relationship("DbAds", back_populates="seller")



class DbCategory(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key= True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    ads = relationship('DbAds', back_populates='category')


class AdStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    RESERVED = "RESERVED"
    SOLD = "SOLD"

class DbAds(Base):
    __tablename__ = 'ads'
    id = Column(Integer, primary_key= True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer)
    status = Column(
        SAEnum(AdStatus, name="ad_status"),
        nullable=False,
        server_default=text("'ACTIVE'"),
    )

    seller_id = Column(Integer, ForeignKey('users.id'))
    seller =relationship('DbUser', back_populates='ads')

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('DbCategory', back_populates='ads')