-- Import the metal_bands table dump first

-- Define a temporary table to store the counts of fans per origin
CREATE TEMPORARY TABLE fan_counts AS
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin;

-- Rank the origins based on the number of fans (non-unique)
SELECT origin, nb_fans,
       RANK() OVER (ORDER BY nb_fans DESC) AS origin_rank
FROM fan_counts
ORDER BY origin_rank;