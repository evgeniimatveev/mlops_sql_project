-- **Product Count by Category** - Counts the number of products in each category.
    
    SELECT category, COUNT(*) AS product_count
    FROM products
    GROUP BY category
    ORDER BY product_count DESC;
    ```