-- 22_top_10_customers_by_spent
SELECT 
    c.customer_id,
    c.name AS customer_name,
    COUNT(o.order_id) AS total_orders,
    SUM(t.amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN transactions t ON o.order_id = t.order_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 10;