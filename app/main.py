from fastapi import FastAPI
from app.api.endpoints import router as catalog_router

app = FastAPI()

app.include_router(catalog_router)


@app.get("/")
def health_check():
    return {"message": "Catalog works"}
