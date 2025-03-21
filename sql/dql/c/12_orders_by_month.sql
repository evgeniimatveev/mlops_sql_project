-- Number of orders per month
SELECT DATE_TRUNC('month', order_date) AS month, COUNT(*) AS total_orders
FROM orders
GROUP BY month
ORDER BY month;