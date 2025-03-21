import psycopg2
import psycopg2.extras
import pandas as pd
from faker import Faker
import random
import re
from tqdm import tqdm
from datetime import datetime, timedelta

# Database connection settings
DB_NAME = "business_analysis"
DB_USER = "postgres"
DB_PASSWORD = "31031987"
DB_HOST = "localhost"
DB_PORT = "5432"

# Initialize Faker
fake = Faker()

# Store generated emails to ensure uniqueness
generated_emails = set()

# Function to generate unique email addresses
def generate_unique_email():
    while True:
        email = fake.email()
        if email not in generated_emails:
            generated_emails.add(email)
            return email

# Function to generate phone numbers in (XXX)XXX-XXXX format
def generate_phone_number():
    phone = fake.phone_number()
    cleaned_phone = re.sub(r'\D', '', phone)  # Remove all non-digit characters
    if len(cleaned_phone) == 10:
        return f"({cleaned_phone[:3]}){cleaned_phone[3:6]}-{cleaned_phone[6:]}"
    elif len(cleaned_phone) > 10:
        return f"({cleaned_phone[-10:-7]}){cleaned_phone[-7:-4]}-{cleaned_phone[-4:]}"
    return "(000)000-0000"  # Default fallback if number is not valid

# Function to generate a random creation date in the last 60 days
def random_datetime():
    return datetime.now() - timedelta(days=random.randint(1, 60), seconds=random.randint(0, 86400))

# Function to generate customer data
def generate_customers(n=5000):
    customers = []
    for _ in tqdm(range(n), desc="Generating Customers"):
        customers.append((
            fake.name(),
            generate_unique_email(),  # Unique email
            generate_phone_number(),  # Formatted phone number
            random_datetime()  # Random creation date
        ))
    return pd.DataFrame(customers, columns=["name", "email", "phone", "created_at"])

# Function to insert data into PostgreSQL
def insert_data(conn, df, table_name, columns):
    try:
        cur = conn.cursor()
        sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES %s ON CONFLICT (email) DO NOTHING"
        tuples = [tuple(x) for x in df.to_numpy()]
        psycopg2.extras.execute_values(cur, sql, tuples)
        conn.commit()
        cur.close()
        print(f"✅ Inserted {len(df)} rows into {table_name}")
    except Exception as e:
        print(f"❌ Error inserting into {table_name}: {e}")

# Run full data generation and insertion process
def generate_and_insert_data():
    try:
        with psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        ) as conn:
            print("✅ Connected to PostgreSQL")

            df_customers = generate_customers(5000)
            insert_data(conn, df_customers, "customers", ["name", "email", "phone", "created_at"])

        print("✅ Database connection closed")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

# Run the function
if __name__ == "__main__":
    generate_and_insert_data()