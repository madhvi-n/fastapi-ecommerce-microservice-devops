from fastapi import FastAPI
from app.api.routes.product import router as product_router
from app.core.database import init_db

app = FastAPI(root_path="/products")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(product_router, prefix="/products", tags=["Products"])
