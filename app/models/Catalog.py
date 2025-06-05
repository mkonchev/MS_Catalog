from app.models.Category import Category
from pydantic import BaseModel, Field


class CatalogItem(BaseModel):
    # item_id: int
    name: str = Field(default=..., description="Название товара")
    category: Category = Field(default=..., description="Категория товара")
    price: int = Field(default=..., description="Цена за штуку")
