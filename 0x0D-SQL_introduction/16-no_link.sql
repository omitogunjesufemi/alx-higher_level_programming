-- A script that list all records of the table skipping rows without a
-- name value
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
