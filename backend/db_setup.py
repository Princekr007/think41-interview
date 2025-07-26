# db_setup.py
from sqlalchemy import create_engine
from models import Base

engine = create_engine('sqlite:///ecommerce.db')  # Will create ecommerce.db in backend folder
Base.metadata.create_all(engine)

print("✅ Database and tables created successfully.")
