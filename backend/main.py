# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/products", response_model=list[schemas.Product])
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.get("/products/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/orders", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@app.get("/inventory/{center_id}", response_model=list[schemas.InventoryItem])
def get_inventory(center_id: int, db: Session = Depends(get_db)):
    return crud.get_inventory(db, center_id)

@app.get("/users/{user_id}/orders", response_model=list[schemas.Order])
def get_user_orders(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_orders(db, user_id)
@app.get("/distribution_centers", response_model=list[schemas.DistributionCenter])
def list_distribution_centers(db: Session = Depends(get_db)):
    return crud.get_distribution_centers(db)
@app.get("/inventory_by_product/{product_id}", response_model=list[schemas.InventoryItem])
def get_inventory_by_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_inventory_by_product(db, product_id)
