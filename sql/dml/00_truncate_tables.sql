-- 00_truncate_tables.sql: Truncate all tables before inserting new data
-- This will remove all records and reset auto-incremented IDs.

TRUNCATE TABLE transactions RESTART IDENTITY CASCADE;
TRUNCATE TABLE orders RESTART IDENTITY CASCADE;
TRUNCATE TABLE products RESTART IDENTITY CASCADE;
TRUNCATE TABLE customers RESTART IDENTITY CASCADE;