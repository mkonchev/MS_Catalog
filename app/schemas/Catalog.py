from app.schemas.models.Category import Category
from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(default=..., description="Название товара")
    category: Category = Field(default=..., description="Категория товара")
    price: int = Field(default=..., description="Цена за штуку")


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int = Field(..., description="ID заказа")

    class Config:
        orm_mode = True
