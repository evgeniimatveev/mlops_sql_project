-- 02_transaction_amount_summary

SELECT 
    MIN(amount) AS min_amount,
    MAX(amount) AS max_amount,
    AVG(amount) AS avg_amount,
    SUM(amount) AS total_amount
FROM transactions;