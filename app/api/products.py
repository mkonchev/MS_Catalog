from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import Catalog as schemas
from app.db.database import SessionLocal
from app.services.product_service import ProductService


router = APIRouter(prefix="/catalog", tags=['catalog'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    service = ProductService(db)
    return service.create_product(product)


@router.get("/", response_model=List[schemas.Product])
def read_all_items(db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_products()


@router.get("/{item_id}", response_model=schemas.Product)
def read_item(item_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_product(item_id)


@router.get("/category/{category}", response_model=List[schemas.Product])
def read_category_items(category: str, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_products_category(category)


@router.get("/{item_id}/exists")
def item_exists(item_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.product_exists(item_id)


@router.put("/{item_id}", response_model=schemas.ProductBase)
def update_product(
    item_id: int,
    upd_item: schemas.ProductUpdate,
    db: Session = Depends(get_db)
):
    service = ProductService(db)
    return service.update_product(upd_item, item_id)


@router.delete("/{item_id}", response_model=schemas.Product)
def delete_product(item_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.delete_product(item_id)
