--  Distribution of order statuses
SELECT status, COUNT(*) 
FROM orders
GROUP BY status;