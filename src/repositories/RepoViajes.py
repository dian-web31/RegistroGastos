import requests
import json
from datetime import date
from src.model.Gasto import Gasto
from src.model.País import País
from src.model.Viaje import Viaje

class RepoViajes:
	'''
	Este repositorio gestiona viajes y sus respectivos gastos,
	además de mantener una copia local de los países que se recuperan de la API.
	'''
	def __init__(self):
		self.viajes: dict[date, Viaje] = {}
		self.países: dict[str, País] = {}
			
	def cargar(self) -> bool:
		'''
		Carga los datos del modelo desde los archivos JSON.\n
		En primera instancia, se intenta cargar los países desde la API \
		https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json.
		Se mantiene una copia estructurada de la información en `países.json`.\n
		:return bool: `True` si se cargó la información contenida en los JSON;
		`False` si los archivos JSON son inválidos.
		'''
		try:
			with open('viaje.json', 'r') as f:
				data = json.load(f)
						
		except FileNotFoundError:
			self.viaje_actual = None
				
	def cargar_países_api(self) -> bool:
		'''
		Carga tasas de cambio desde API externa
		:return bool: `True` si la API dio respuesta;
		`False` si la comunicación falló.
		'''
		url_tasas = "https://latest.currency-api.pages.dev/v1/currencies/cop.json"
		url_nombres = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json"
		url_alfa2 = "https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.json"

		# 1. Tasas de cambio respecto al COP
		tasas_response = requests.get(url_tasas).json()["cop"]

		# 2. Nombre de cada divisa (no usado en esta versión)
		nombres_response = requests.get(url_nombres).json()

		# 3. ISO ALPHA2 y mapeo divisa (lo agregas tú manualmente o desde una fuente)
		alfa2_divisas = {
			"US": "usd",
			"AR": "ars",
			"CO": "cop",
			"MX": "mxn",
			"PE": "pen",
			"CL": "clp",
			# ... puedes completarlo o cargarlo desde un JSON externo
		}

		# 4. Simular mapeo de alfa2 con nombre país (si no tienes una fuente completa)
		alfa2_nombres = {
			"US": "Estados Unidos",
			"AR": "Argentina",
			"CO": "Colombia",
			"MX": "México",
			"PE": "Perú",
			"CL": "Chile"
		}

		# 5. Crear objetos País
		for alfa2, codigo_divisa in alfa2_divisas.items():
			if codigo_divisa in tasas_response:
				nombre = alfa2_nombres.get(alfa2, "Desconocido")
				tasa = tasas_response[codigo_divisa]
				pais = País(alfa2, nombre, codigo_divisa, tasa)
				self.paises[alfa2] = pais
			
	def guardar_viaje(self, viaje: Viaje) -> bool:
		'''Guarda un nuevo viaje'''
		if self.viaje_actual:
			with open('viaje.json', 'w') as f:
				json.dump(self.viaje_actual.to_dict(), f)
			
	def guardar_gasto(self, gasto: Gasto) -> bool:
		'''Guarda un gasto asociado a un viaje'''
		pass
			
	def buscar_viaje(self, fecha: date) -> 'Viaje':
		'''Busca viaje por fecha de inicio'''
		pass
			
	def buscar_país(self, alfa2: str) -> 'País':
		"""TODO: Busqueda del país por su código alfa2"""
    	pass

			