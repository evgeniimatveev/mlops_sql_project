-- 03_constraints.sql: Adding constraints
-- Ensure email is unique
ALTER TABLE customers ADD CONSTRAINT unique_email UNIQUE (email);

-- Ensure price and amount are positive
ALTER TABLE products ADD CONSTRAINT positive_price CHECK (price > 0);
ALTER TABLE transactions ADD CONSTRAINT positive_amount CHECK (amount > 0);

-- Ensure stock quantity is non-negative
ALTER TABLE products ADD CONSTRAINT non_negative_stock CHECK (stock_quantity >= 0);