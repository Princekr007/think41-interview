# init_db.py

from models import Base
from database import engine  # import engine from your existing config

# Create all tables from models
Base.metadata.create_all(engine)

print("✅ All tables created.")
