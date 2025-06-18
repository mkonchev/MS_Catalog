from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from app.models.Catalog import CatalogItem
from app.database import DBCatalogItem, get_db
from typing import List

router = APIRouter(prefix="/catalog", tags=['catalog'])

# резделить по категории и каталог_итем
@router.post("/", response_model=CatalogItem)
def create_item(item: CatalogItem, db: Session = Depends(get_db)):
    db_item = DBCatalogItem(
        name=item.name,
        category=item.category,
        price=item.price
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# @router.get("/")
# def homepage():
#     return JSONResponse({'message': 'Welcome to the API'})


@router.get("/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(DBCatalogItem).filter(DBCatalogItem.id == item_id).first()
    if not item:
        return JSONResponse({"error": "Item not found"}, status_code=404)
    return item


@router.get("/", response_model=List[CatalogItem])
def read_all_items(
    db: Session = Depends(get_db)
):
    items = db.query(DBCatalogItem).all()
    return items
