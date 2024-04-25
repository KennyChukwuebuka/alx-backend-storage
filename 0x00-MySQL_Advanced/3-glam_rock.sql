-- Import the metal_bands table dump first

-- List all bands with Glam rock as their main style and calculate their lifespan
-- CTE
SELECT band_name, (IFNULL(split, YEAR(CURDATE())) - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC