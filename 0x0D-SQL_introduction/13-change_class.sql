-- A script that removes all records with a score <= 5 from the table to
-- be displayed
SELECT score, name
FROM second_table
WHERE score > 5
ORDER BY score DESC;
