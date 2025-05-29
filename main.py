from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse
from typing import Literal


class CatalogItem(BaseModel):
    name: str
    category: Literal[1, 2, 3, 4, 5]
    price: int


app = FastAPI()


@app.post("/create_items/{item_id}")
def create_item(item: CatalogItem, item_id: int):
    return JSONResponse({"item": item.model_dump(), "item_id": item_id})


@app.get("/")
def homepage():
    return JSONResponse({'ты че тут забыл': '?'})


@app.get("/get_items/{item_id}")
def read_item(item_id: int):
    print("item_id", item_id)
    return {"item_id": item_id}
