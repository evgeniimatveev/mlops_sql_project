SQL File Organization
 
DQL (Data Analysis & Reporting)

A. Data Validation & Structure

01_check_constraints.sql → Retrieves all table constraints.
02_check_all_foreign_keys.sql → Displays all foreign keys and referenced tables.
03_check_table_dependencies.sql → Finds dependencies between tables.
04_check_indexes_primary_keys.sql → Lists indexes and primary keys.
05_check_privileges.sql → Lists user privileges for security validation.

B. Aggregation & Statistical Analysis

06_table_counts.sql → Counts total rows in all tables (high-level check).
07_check_total_records.sql → Verifies record consistency (validation).
08_counts_the_number_of_products.sql → Finds duplicate product names.
09_min_max_and_average_price.sql → Calculates min/max/avg product prices.
10_stock_statistics.sql → Analyzes stock min/max/avg quantities.

C. Orders & Transactions

11_top_expensive_orders.sql → Retrieves top 10 highest-value orders.
12_orders_by_month.sql → Aggregates the number of orders per month.
13_random_orders_check.sql → Selects a random sample of orders for validation.
14_customers_orders_join.sql → Joins customers & orders for detailed insights.
15_transaction_amount_summary.sql → Summarizes total transaction amounts.
16_transactions_by_payment.sql → Aggregates transactions by payment method.
17_daily_transaction_volume.sql → Analyzes daily transaction volume.
18_top_10_biggest_transactions.sql → Retrieves top 10 highest-value transactions.
19_top_10_biggest_customers.sql → Retrieves the top 10 biggest customers.

d. Joints

20_join_customers_orders_products.sql → Customers x Orders x Products
21_join_orders_transactions.sql   → Orders x Transactions
22_top_10_customers_by_spent.sql → Retrieves the top 10 customers based on total transaction amount.
23_avg_order_value.sql → Calculates the average order value per customer.
24_returning_customers.sql → Identifies returning customers (more than 1 order).
25_bonus.sql → Executes a special bonus query for additional insights.
26_cleaned_bonus.sql → Refines 25_bonus.sql by replacing NULL values with meaningful defaults. 