\c calyx2
DROP TABLE IF EXISTS cultural;

CREATE TABLE IF NOT EXISTS cultural (
	index int NOT NULL,
	cod_localidad int NOT NULL,
	id_provincia int NOT NULL,
	id_departamento int NOT NULL,
	categoria text DEFAULT NULL,
	provincia text DEFAULT NULL,
	localidad text DEFAULT NULL,
	nombre text DEFAULT NULL,
	domicilio text DEFAULT NULL,
	cod_postal text DEFAULT NULL,
	n_telefono text DEFAULT NULL,
	mail text DEFAULT NULL,
	web text DEFAULT NULL
);
