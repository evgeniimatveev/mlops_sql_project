--  Top 10 most expensive orders
SELECT * FROM orders
ORDER BY total_amount DESC
LIMIT 10;