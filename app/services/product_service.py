from sqlalchemy.orm import Session
from fastapi import HTTPException
from services.MS_Catalog.app.schemas import Catalog as schemas
from services.MS_Catalog.app.crud import products as crud


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product: schemas.ProductCreate):
        return crud.create_product(self.db, product)

    def get_products(self):
        return crud.get_products(self.db)

    def product_exists(self, product_id: int):
        if crud.get_product(self.db, product_id):
            return True
        else:
            return False

    def get_products_category(self, category: str):
        return crud.get_products_category(self.db, category)

    def get_product(self, product_id: int):
        product = crud.get_product(self.db, product_id)
        if product:
            return product
        else:
            raise HTTPException(status_code=404, detail="Not Found")

    def update_product(self, product: schemas.ProductUpdate, product_id: int):
        product = crud.update_product(self.db, product_id, product)
        if product:
            return product
        else:
            raise HTTPException(status_code=404, detail="Not Found")

    def delete_product(self, product_id: int):
        product = crud.delete_product(self.id, product_id)
        if product:
            return product
        else:
            raise HTTPException(status_code=404, detail="Not Found")
