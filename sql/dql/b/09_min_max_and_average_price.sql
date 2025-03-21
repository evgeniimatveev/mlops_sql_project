 -- Price Statistics - Retrieves min, max, and average price of products.
   
    SELECT MIN(price) AS min_price, MAX(price) AS max_price, AVG(price) AS avg_price
    FROM products;
    