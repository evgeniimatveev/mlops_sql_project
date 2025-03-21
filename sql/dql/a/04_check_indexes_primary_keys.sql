--  Check indexes and primary keys for all tables
SELECT tablename, 
       indexname, 
       indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename;