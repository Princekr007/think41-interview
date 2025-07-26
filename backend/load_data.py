import csv
from models import Product, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup SQLite database (or use any URI you want)
engine = create_engine('sqlite:///data/ecommerce.db')  # Make sure data/ folder exists
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

def load_products():
    with open('data/products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = Product(
                id=int(row['id']),
                name=row['name'],
                category=row['category'],  # Make sure your CSV uses 'category'
                price=float(row['price'])
            )
            session.add(product)
        session.commit()
        print("✅ Products loaded.")

if __name__ == '__main__':
    load_products()
