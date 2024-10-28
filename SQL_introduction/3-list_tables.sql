--  list all the tables of a database
SELECT table_name
FROM information_schema.tables
WHERE table_type='BASE TABLE';