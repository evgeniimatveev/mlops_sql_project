--  Check all constraints in the database
SELECT conname AS constraint_name, 
       conrelid::regclass AS table_name, 
       pg_get_constraintdef(oid) AS constraint_definition
FROM pg_constraint
ORDER BY table_name;