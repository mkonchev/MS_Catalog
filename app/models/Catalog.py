from app.models.Category import Category
from pydantic import BaseModel, Field


# переименовать
class CatalogItem(BaseModel):
    id: int = Field(..., description="ID заказа")
    name: str = Field(default=..., description="Название товара")
    category: Category = Field(default=..., description="Категория товара")
    price: int = Field(default=..., description="Цена за штуку")
