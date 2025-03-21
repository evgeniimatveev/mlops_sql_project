--  Check all foreign keys and their referenced tables
SELECT conname AS constraint_name, 
       conrelid::regclass AS table_name, 
       confrelid::regclass AS referenced_table
FROM pg_constraint
WHERE contype = 'f' -- 'f' means foreign key
ORDER BY table_name;