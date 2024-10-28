-- list the number of records with the same score in the table second_table of the database
SELECT score, count(score)
  FROM second_table
GROUP BY score;