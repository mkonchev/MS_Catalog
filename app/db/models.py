from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from app.schemas.models.Category import Category as CategoryEnum
from app.db.database import engine

Base = declarative_base()

# PRODUCT_CATEGORIES = ['clothes', 'food', 'another']


class Product(Base):
    __tablename__ = "catalog_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    category = Column(Enum(CategoryEnum, native_enum=False))
    price = Column(Integer)


Base.metadata.create_all(bind=engine)
