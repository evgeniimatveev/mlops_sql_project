--  Fetch 10 random orders for data validation
SELECT * FROM orders
ORDER BY RANDOM()
LIMIT 10;