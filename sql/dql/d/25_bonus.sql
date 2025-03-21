-- 25_bonus
SELECT 
    c.customer_id,
    c.name AS customer_name,
    o.order_id,
    o.order_date,
    o.status AS order_status,
    t.transaction_id,
    t.payment_method,
    t.transaction_date,
    t.amount AS transaction_amount,
    p.product_id,
    p.name AS product_name,
    p.category AS product_category,
    p.price AS product_price,
    p.stock_quantity
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN transactions t ON o.order_id = t.order_id
LEFT JOIN products p ON t.transaction_id = p.product_id
ORDER BY c.customer_id, o.order_date DESC;