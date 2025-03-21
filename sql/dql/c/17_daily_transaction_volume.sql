-- 18_daily_transaction_volumeм
SELECT 
    DATE(transaction_date) AS transaction_day,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY transaction_day
ORDER BY transaction_day;
