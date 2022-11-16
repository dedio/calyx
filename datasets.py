import os
import requests
from lxml import html
from datetime import date
from pathlib import Path

cultural = {
	'museos': 'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d',
	'cines': 'https://datos.gob.ar/vi/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_f7a8edb8-9208-41b0-8f19-d72811dcea97',
	'bibliotecas': 'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7'
}
meses = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

def trae_ficheros():
	hoy = date.today()
	for c in cultural:
		page = requests.get(cultural[c])
		tree = html.fromstring(page.content)
		csv = ''.join(tree.xpath('//a[@class="btn btn-green btn-block"]/@href'))
		filename = c + hoy.strftime('%d-%m-%Y') + '.csv'
		ruta = c + '/' + hoy.strftime('%Y') + '-' + meses[hoy.month -1]
		path = Path(ruta)
		if not path.exists():
			path.mkdir(parents=True)
		with open((ruta + '\\' + filename), 'wb') as f:
			s = requests.get(csv)
			f.write(s.content)
			f.close()
