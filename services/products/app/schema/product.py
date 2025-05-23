from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    title: str
    slug: str
    description: Optional[str] = None
    price: float
    currency: str = "USD"
    in_stock: bool = True
    stock_qty: int = 0
    category: Optional[str]
    brand: Optional[str]
    image_url: Optional[str]


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    currency: Optional[str]
    in_stock: Optional[bool]
    stock_qty: Optional[int]
    category: Optional[str]
    brand: Optional[str]
    image_url: Optional[str]


class ProductOut(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
