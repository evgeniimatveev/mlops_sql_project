--  Join customers and orders to check latest orders
SELECT 
    c.customer_id, 
    c.name, 
    c.email, 
    o.order_id, 
    o.order_date, 
    o.status, 
    o.total_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
ORDER BY o.order_date DESC
LIMIT 10;