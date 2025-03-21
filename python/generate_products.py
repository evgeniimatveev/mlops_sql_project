import random
import psycopg2
from faker import Faker
import uuid

# Initialize Faker
faker = Faker()

# PostgreSQL connection details
DB_PARAMS = {
    "dbname": "business_analysis",
    "user": "postgres",
    "password": "31031987",
    "host": "localhost",
    "port": "5432"
}

# Product categories
CATEGORIES = ["Electronics", "Clothing", "Books", "Furniture", "Toys"]

# Function to generate unique random products
def generate_products(n=5000):
    products = set()  # Using a set to ensure uniqueness
    while len(products) < n:
        product_name = f"{faker.word().capitalize()}_{uuid.uuid4().hex[:6]}_{random.randint(1000,9999)}"  
        product = (
            product_name,  # Unique name
            random.choice(CATEGORIES),  # Category
            round(random.uniform(5, 500), 2),  # Price
            random.randint(0, 100)  # Stock quantity
        )
        products.add(product)  # Ensure uniqueness
    return list(products)

# Insert generated products into the database
def insert_products(products):
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()

        query = """
        INSERT INTO products (name, category, price, stock_quantity)
        VALUES (%s, %s, %s, %s)
        """
        cursor.executemany(query, products)

        conn.commit()
        print(f"✅ Inserted {len(products)} products into the database.")

    except psycopg2.DatabaseError as e:
        print(f"❌ Database error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        cursor.close()
        conn.close()
        print("✅ Database connection closed.")

if __name__ == "__main__":
    print("🚀 Generating 5000 random products...")
    products_data = generate_products(5000)
    insert_products(products_data)