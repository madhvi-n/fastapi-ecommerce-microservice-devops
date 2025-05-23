from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schema.product import ProductCreate, ProductOut, ProductUpdate
from app.services.product import (
    create_product,
    get_product,
    get_all_products,
    update_product,
    delete_product,
)
from app.core.database import get_db
from app.core.utils.auth import staff_or_admin_required


router = APIRouter()

@router.post("/", response_model=ProductOut, dependencies=[Depends(staff_or_admin_required)])
def create(item: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, item)

@router.get("/", response_model=list[ProductOut])
def read_all(db: Session = Depends(get_db)):
    return get_all_products(db)

@router.get("/{product_id}", response_model=ProductOut)
def read(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductOut, dependencies=[Depends(staff_or_admin_required)])
def update(product_id: int, item: ProductUpdate, db: Session = Depends(get_db)):
    return update_product(db, product_id, item)

@router.delete("/{product_id}", dependencies=[Depends(staff_or_admin_required)])
def delete(product_id: int, db: Session = Depends(get_db)):
    delete_product(db, product_id)
    return {"detail": "Deleted"}
