import pandas as pd
import psycopg2
import os

print("🚀 Script started...")

# Connecting to the PostgreSQL database
try:
    print("🔌 Connecting to database...")
    conn = psycopg2.connect(
        dbname="business_analysis",
        user="postgres",
        password="31031987",
        host="localhost",
        port="5432"
    )
    print("✅ Connection successful!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    exit()

# SQL query: Customer behavior analysis
query = """
SELECT 
    o.customer_id, 
    COUNT(t.order_id) AS total_orders, 
    SUM(t.amount) AS total_spent, 
    AVG(t.amount) AS avg_order_value, 
    MAX(t.transaction_date) AS last_purchase_date
FROM transactions t
JOIN orders o ON t.order_id = o.order_id
GROUP BY o.customer_id
ORDER BY total_spent DESC;
"""

try:
    print("🔄 Running SQL query...")
    df = pd.read_sql(query, conn)
    print(f"✅ SQL query executed! DataFrame shape: {df.shape}")

    if df.empty:
        print("⚠️ Warning: The query returned an empty DataFrame!")

    # ✅ Ensure the directory path is absolute
    excel_dir = os.path.abspath("excel")  # Generate an absolute path

    # ✅ Check if the directory exists
    if not os.path.exists(excel_dir):
        print(f"⚠️ Warning: Directory does not exist! Creating: {excel_dir}")
        os.makedirs(excel_dir)

    # ✅ Create the full path for the Excel file
    excel_path = os.path.join(excel_dir, "customer_behavior.xlsx")
    print(f"💾 Saving file to: {excel_path}")

    # ✅ Save the DataFrame to an Excel file
    df.to_excel(excel_path, index=False, engine="openpyxl")
    print(f"📊 Customer behavior report saved successfully at: {excel_path}!")

except Exception as e:
    print(f"❌ Error executing SQL or saving Excel: {e}")

finally:
    conn.close()
    print("🔒 Connection closed.")