-- 02_create_tables.sql: Creating tables
-- Customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY, -- Unique ID for each customer
    name VARCHAR(100) NOT NULL, -- Customer's full name
    email VARCHAR(100) UNIQUE NOT NULL, -- Unique email address for each customer
    phone VARCHAR(30), -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the record was created
);

-- Products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY, -- Unique ID for each product
    name VARCHAR(255) NOT NULL, -- Product name
    category VARCHAR(100), -- Product category (e.g., Electronics, Home)
    price DECIMAL(10,2) NOT NULL, -- Price of the product
    stock_quantity INT NOT NULL -- Available stock quantity
);

-- Orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY, -- Unique ID for each order
    customer_id INT NOT NULL, -- Foreign key linking to the customers table
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    status VARCHAR(50) CHECK (status IN ('pending', 'shipped', 'delivered', 'cancelled')), -- Order status
    total_amount DECIMAL(10,2) NOT NULL, -- Total amount of the order
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) -- Linking to the customers table
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique ID for each transaction
    order_id INT NOT NULL, -- Foreign key linking to the orders table
    payment_method VARCHAR(50) CHECK (payment_method IN ('credit_card', 'paypal', 'bank_transfer')), -- Payment method used
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    amount DECIMAL(10,2) NOT NULL, -- Transaction amount
    FOREIGN KEY (order_id) REFERENCES orders(order_id) -- Linking to the orders table
);