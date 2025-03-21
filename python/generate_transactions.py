import psycopg2
import random
from faker import Faker

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

# Payment methods
PAYMENT_METHODS = ["credit_card", "paypal", "bank_transfer"]

# Generate transactions
def generate_transactions(n=5000):
    print("🔹 Generating transactions...")

    transactions = []
    for transaction_id in range(1, n + 1):
        order_id = random.randint(1, 5000)  # Ensure order_id exists
        payment_method = random.choice(PAYMENT_METHODS)
        transaction_date = faker.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S")
        amount = round(random.uniform(10, 1000), 2)

        transaction = (transaction_id, order_id, payment_method, transaction_date, amount)
        transactions.append(transaction)

    print(f"✅ {len(transactions)} transactions generated successfully.")
    print(f"🔍 Sample transactions: {transactions[:5]}")  # Debug: print first 5 records
    return transactions

def insert_transactions(transactions):
    print("🔹 Connecting to the database...")

    try:
        # Test connection
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()
        print("✅ Connected to PostgreSQL.")

        # Run a simple query to confirm connection
        cursor.execute("SELECT 1;")
        print(f"🟢 Connection test successful: {cursor.fetchone()}")

        # SQL query to insert transactions
        query = """
        INSERT INTO transactions (transaction_id, order_id, payment_method, transaction_date, amount)
        VALUES (%s, %s, %s, %s, %s);
        """
        
        print(f"🔍 First 5 transactions: {transactions[:5]}")  # Debugging output
        print(f"📝 Preparing batch insert of {len(transactions)} records...")

        # Execute batch insert
        cursor.executemany(query, transactions)
        conn.commit()

        print(f"✅ Successfully inserted {len(transactions)} transactions into the database.")

    except psycopg2.DatabaseError as e:
        print(f"❌ Database error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        conn.commit()  # Ensure commit before closing
        cursor.close()
        conn.close()
        print("🔹 Database connection closed.")

if __name__ == "__main__":
    transactions_data = generate_transactions(5000)
    if transactions_data:
        insert_transactions(transactions_data)
    else:
        print("❌ No transactions generated. Check the generation logic.")