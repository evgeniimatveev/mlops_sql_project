--  Check privileges for all tables (who has access to what)
SELECT grantee, 
       privilege_type, 
       table_name
FROM information_schema.role_table_grants
WHERE table_schema = 'public'
ORDER BY table_name;