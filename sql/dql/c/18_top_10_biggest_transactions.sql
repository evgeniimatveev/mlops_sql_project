-- 05_top_10_biggest_transactions 
SELECT * 
FROM transactions
ORDER BY amount DESC
LIMIT 10;