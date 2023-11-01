-- 2-fans.sql
-- script can be executed on any database

SELECT band_name,
  IFNULL(split, YEAR(CURDATE())) - formed AS lifespan
FROM
  metal_bands
WHERE
  main_style = 'Glam rock'
ORDER BY
  lifespan DESC;