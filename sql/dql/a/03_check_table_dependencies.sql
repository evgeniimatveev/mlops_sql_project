-- ✅ Check which tables reference a specific table (dependencies)
SELECT conrelid::regclass AS referencing_table, 
       confrelid::regclass AS referenced_table, 
       conname AS constraint_name
FROM pg_constraint
WHERE confrelid = 'orders'::regclass  -- Change 'orders' to any table you want to check
ORDER BY referencing_table;