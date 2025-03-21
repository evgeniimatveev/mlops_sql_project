-- 26_Cleaned_bonus
SELECT 
    c.customer_id,
    c.name AS customer_name,
    COALESCE(o.order_id, 'No Order') AS order_id,
    COALESCE(o.order_date, '1900-01-01') AS order_date,
    COALESCE(o.status, 'No Order') AS order_status,
    COALESCE(t.transaction_id, 'No Transaction') AS transaction_id,
    COALESCE(t.payment_method, 'No Payment') AS payment_method,
    COALESCE(t.transaction_date, '1900-01-01') AS transaction_date,
    COALESCE(t.amount, 0) AS transaction_amount,
    COALESCE(p.product_id, 'No Product') AS product_id,
    COALESCE(p.name, 'No Product') AS product_name,
    COALESCE(p.category, 'No Category') AS product_category,
    COALESCE(p.price, 0) AS product_price,
    COALESCE(p.stock_quantity, 0) AS stock_quantity
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN transactions t ON o.order_id = t.order_id
LEFT JOIN products p ON t.transaction_id = p.product_id 
ORDER BY c.customer_id, o.order_date DESC;