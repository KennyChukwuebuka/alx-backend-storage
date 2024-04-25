-- 0x00-MySQL_Advanced/2-fans.sql
SELECT 
  origin, 
  COUNT(*) as nb_fans
FROM 
  metal_bands
GROUP BY 
  origin
ORDER BY 
  nb_fans DESC;