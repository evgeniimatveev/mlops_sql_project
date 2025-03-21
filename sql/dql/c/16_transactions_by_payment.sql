-- 17_transactions_by_payment_method
SELECT 
    payment_method,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY payment_method
ORDER BY total_amount DESC;