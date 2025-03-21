-- 24_returning_customer
SELECT 
    c.customer_id,
    c.name AS customer_name,
    COUNT(o.order_id) AS total_orders,
    SUM(t.amount) AS total_spent,
    ROUND(AVG(t.amount), 2) AS avg_order_value
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN transactions t ON o.order_id = t.order_id
GROUP BY c.customer_id, c.name
ORDER BY avg_order_value DESC;