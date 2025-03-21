import pandas as pd
import psycopg2
import openpyxl

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="business_analysis",
    user="postgres",
    password="31031987",
    host="localhost",
    port="5432"
)

# SQL Query: Aggregate sales data by month
query = """
SELECT 
    DATE_TRUNC('month', transaction_date) AS month,  
    COUNT(order_id) AS total_orders,
    SUM(amount) AS total_revenue,
    AVG(amount) AS avg_order_value
FROM transactions
GROUP BY month
ORDER BY month;
"""

# Execute query and load into DataFrame
df = pd.read_sql(query, conn)

# Format column names
df.columns = ["Month", "Total Orders", "Total Revenue", "Avg Order Value"]

# Convert Month column to YYYY-MM format
df["Month"] = df["Month"].dt.strftime("%Y-%m")

# Round numbers to 2 decimal places
df["Total Revenue"] = df["Total Revenue"].round(2)
df["Avg Order Value"] = df["Avg Order Value"].round(2)

# Add Grand Total row
grand_total = pd.DataFrame({
    "Month": ["Grand Total"],
    "Total Orders": [df["Total Orders"].sum()],
    "Total Revenue": [df["Total Revenue"].sum()],
    "Avg Order Value": [df["Avg Order Value"].sum()]
})

df = pd.concat([df, grand_total], ignore_index=True)

# Save the DataFrame to Excel
df.to_excel("./Excel/sales_summary.xlsx", index=False, engine="openpyxl")

# Auto-adjust column width
wb = openpyxl.load_workbook("./Excel/sales_summary.xlsx")
ws = wb.active

for col in ws.columns:
    max_length = 0
    col_letter = col[0].column_letter  # Get column letter (A, B, C, etc.)
    for cell in col:
        try:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        except:
            pass
    ws.column_dimensions[col_letter].width = max_length + 2  # Adjust width

wb.save("./Excel/sales_summary.xlsx")
wb.close()

print("✅ Sales summary report updated successfully!")

# Close database connection
conn.close()