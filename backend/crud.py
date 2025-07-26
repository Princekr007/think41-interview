# crud.py

from sqlalchemy.orm import Session
from models import Product, Order, InventoryItem
import schemas
from fastapi import HTTPException

def get_products(db: Session):
    return db.query(Product).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_inventory(db: Session, center_id: int):
    return db.query(InventoryItem).filter(InventoryItem.center_id == center_id).all()

def get_user_orders(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).all()

def create_order(db: Session, order: schemas.OrderCreate):
    # Step 1: Check product exists
    product = db.query(Product).filter(Product.id == order.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Step 2: Get all inventory with this product
    inventory_items = (
        db.query(InventoryItem)
        .filter(InventoryItem.product_id == order.product_id)
        .filter(InventoryItem.quantity > 0)
        .order_by(InventoryItem.quantity.desc())  # prioritize large stock
        .all()
    )

    total_available = sum(item.quantity for item in inventory_items)
    if total_available < order.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")

    # Step 3: Deduct stock from centers
    quantity_needed = order.quantity
    for item in inventory_items:
        if quantity_needed == 0:
            break
        deduct = min(item.quantity, quantity_needed)
        item.quantity -= deduct
        quantity_needed -= deduct

    # Step 4: Save order
    new_order = Order(
        product_id=order.product_id,
        user_id=order.user_id,
        quantity=order.quantity
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order
def get_distribution_centers(db: Session):
    return db.query(models.DistributionCenter).all()
# crud.py

def get_inventory_by_product(db: Session, product_id: int):
    return db.query(models.InventoryItem).filter(models.InventoryItem.product_id == product_id).all()
