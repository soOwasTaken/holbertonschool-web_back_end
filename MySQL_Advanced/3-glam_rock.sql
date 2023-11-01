-- 3-glam_rock.sql
-- script can be executed on any database

SELECT DISTINCT band_name,
                IFNULL(`split`, 2020) - formed as lifespan
    FROM metal_bands WHERE FIND_IN_SET('Glam rock', style)
    ORDER BY `lifespan` DESC;