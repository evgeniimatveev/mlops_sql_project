-- 20_join_customers_orders_products
SELECT 
    c.customer_id, 
    c.name AS customer_name, 
    o.order_id, 
    o.order_date, 
    p.product_id, 
    p.name AS product_name, 
    t.amount AS transaction_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN transactions t ON o.order_id = t.order_id
JOIN products p ON o.order_id = p.product_id 
ORDER BY c.customer_id, o.order_date DESC;