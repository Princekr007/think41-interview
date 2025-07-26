# schemas.py
from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    description: str
    price: float

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class Order(OrderCreate):
    id: int
    order_date: datetime
    class Config:
        orm_mode = True

class InventoryItem(BaseModel):
    product_id: int
    quantity: int
    class Config:
        orm_mode = True
# schemas.py

from pydantic import BaseModel

class DistributionCenter(BaseModel):
    id: int
    name: str
    location: str

    class Config:
        from_attributes = True  # ✅ for Pydantic v2 compatibility
