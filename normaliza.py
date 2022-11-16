import os
import fnmatch
import pandas as pd
from sqlalchemy import create_engine

directorios = ['bibliotecas', 'cines', 'museos']
columnas = {
	'bibliotecas':[
		'Cod_Loc',
		'IdProvincia',
		'IdDepartamento',
		'Categoría',
		'Provincia',
		'Localidad',
		'Nombre',
		'Domicilio',
		'CP',
		'Teléfono',
		'Mail',
		'Web'
	],
	'cines':[
		'cod_localidad',
		'id_provincia',
		'id_departamento',
		'categoria',
		'provincia',
		'localidad',
		'nombre',
		'direccion',
		'cp',
		'web'
	],
	'museos':[
		'Cod_Loc',
		'IdProvincia',
		'IdDepartamento',
		'subcategoria',
		'provincia',
		'localidad',
		'nombre',
		'direccion',
		'CP',
		'telefono',
		'Mail',
		'Web'
	]
}

normal = [
	'cod_localidad',
	'id_provincia',
	'id_departamento', 
	'categoria',
	'provincia',
	'localidad',
	'nombre',
	'domicilio',
	'cod_postal',
	'n_telefono',
	'mail',
	'web'
]
target = '*.csv'

def normalizaypuebla():
	engine = create_engine("postgresql://user:pass@localhost/calyx2")
	for initial_dir in directorios:
		path_list = [
			os.path.join(root, file) 
			for root, _, files in os.walk(initial_dir)
				for file in fnmatch.filter(files, target)
		]
		path_list.sort(key=os.path.getmtime)

		dataset = pd.read_csv(path_list[-1])

		# Normalización
		for c in dataset.columns:
			if not c in columnas[initial_dir]:
				dataset = dataset.drop(c, axis=1)
		if not 'Teléfono' in dataset.columns and not 'telefono' in dataset.columns:
			dataset['telefono'] = "NULL"
		if not 'Mail' in dataset.columns and not 'mail' in dataset.columns:
			dataset['mail'] = "NULL"
		dataset.columns = normal
		dataset.to_sql('cultural', engine, if_exists='append', chunksize=1000)
