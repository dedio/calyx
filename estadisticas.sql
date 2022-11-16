\c calyx2

-- ~ Cantidad de registros totales por categoría
SELECT COUNT(*), categoria INTO TABLE porcategoria FROM cultural GROUP BY categoria;
-- ~ Cantidad de registros por provincia y categoría
SELECT COUNT(*), provincia, categoria INTO TABLE porprovinciaycategoria FROM cultural GROUP BY provincia, categoria;
