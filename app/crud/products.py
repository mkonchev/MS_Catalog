from sqlalchemy.orm import Session
from services.MS_Catalog.app.schemas import Catalog as schemas
from services.MS_Catalog.app.db import models


def create_product(db: Session, product: schemas.ProductCreate):
    db_item = models.Product(**product.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_products(db: Session):
    return db.query(models.Product).all()


def get_products_category(db: Session, category: str):
    return db.query(
        models.Product
        ).filter(
        models.Product.category == category
        ).all()


def get_product(db: Session, product_id: int):
    return db.query(
        models.Product
        ).filter(
        models.Product.id == product_id
        ).first()


def update_product(
        db: Session,
        product_id: int,
        upd_product: schemas.ProductUpdate,
):
    db_item = get_product(db, product_id)
    if db_item:
        db_item.name = upd_product.name,
        db_item.category = upd_product.category,
        db_item.price = upd_product.price,
        db.commit()
        db.refresh(db_item)
    return db_item


def delete_product(db: Session, product_id: int):
    db_item = get_product(db, product_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
