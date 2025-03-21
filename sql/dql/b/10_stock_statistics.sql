-- Stock Statistics - Retrieves min, max, and average stock quantity of products.
    
    SELECT 
        MIN(stock_quantity) AS min_stock,
        MAX(stock_quantity) AS max_stock,
        AVG(stock_quantity) AS avg_stock
    FROM products;
   