-- A script that list the umber of records with the same score in the
-- table
SELECT score, COUNT(name) AS "number"
FROM second_table
GROUP BY score
ORDER BY score DESC;
