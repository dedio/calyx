from datasets import *
from normaliza import *
import psycopg2

if __name__ == __main__:
	# ~ Conexión a la base de datos
	conn_string = "host='localhost' dbname='calyx2' user='postgres' password='secret'"
	conn = psycopg2.connect(conn_string)
	cursor = conn.cursor()
	
	# ~ Inicia la tabla cultural
	cursor.execute(open("database.sql", "r").read())
	
	trae_ficheros()
	normalizaypuebla()


	# ~ Cantidad de registros totales por categoría
	porcategoria = 'SELECT COUNT(*), categoria INTO TABLE porcategoria FROM cultural GROUP BY categoria'
	# ~ Cantidad de registros por provincia y categoría
	porprovinciaycategoria = '\
		SELECT \
		COUNT(*),\
		provincia, \
		categoria \
		INTO TABLE \
			porprovinciaycategoria \
		FROM \
			cultural \
		GROUP BY \
			provincia, \
			categoria'

	cursor.execute(porcategoria)
	res_porcategoria = cursor.fetchall()
	print(res_porcategoria)
	
	cursor.execute(porprovinciaycategoria)
	res_porprovinciaycategoria = cursor.fetchall()
	print(res_porprovinciaycategoria)
