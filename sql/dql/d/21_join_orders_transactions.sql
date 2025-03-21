SELECT 
    o.order_id, 
    o.order_date, 
    o.status, 
    t.transaction_id, 
    t.payment_method, 
    t.transaction_date, 
    t.amount AS transaction_amount
FROM orders o
JOIN transactions t ON o.order_id = t.order_id
ORDER BY o.order_date DESC;