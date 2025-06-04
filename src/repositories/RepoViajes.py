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
		pass
			
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
		'''Busca país por código'''
			