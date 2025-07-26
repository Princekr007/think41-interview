from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)

class DistributionCenter(Base):
    __tablename__ = 'distribution_centers'
    id = Column(Integer, primary_key=True)
    name = Column(String)   # Keep this one (not just 'location')
    location = Column(String)
    capacity = Column(Integer)

class InventoryItem(Base):
    __tablename__ = 'inventory_items'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    distribution_center_id = Column(Integer, ForeignKey('distribution_centers.id'))
    quantity = Column(Integer)

    product = relationship("Product")
    distribution_center = relationship("DistributionCenter")

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    order_date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User")
    product = relationship("Product")
