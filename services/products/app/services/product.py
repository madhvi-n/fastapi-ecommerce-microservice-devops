from sqlalchemy.orm import Session
from app.models.product import Product
from app.schema.product import ProductCreate, ProductUpdate

def create_product(db: Session, item: ProductCreate):
    product = Product(**item.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_all_products(db: Session):
    return db.query(Product).all()

def update_product(db: Session, product_id: int, item: ProductUpdate):
    product = get_product(db, product_id)
    if not product:
        return None
    for field, value in item.dict(exclude_unset=True).items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    if product:
        db.delete(product)
        db.commit()
