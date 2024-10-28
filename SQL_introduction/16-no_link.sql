-- list all records of the table second_table of the database
-- Don’t list rows without a name value
-- display the score and the name (in this order)
-- listed by descending score
SELECT score, name
  FROM second_table
 WHERE name IS NOT NULL
 ORDER BY score DESC, name DESC;