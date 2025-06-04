from dotenv import load_dotenv
load_dotenv()

import os
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

	# TODO - El retorno debe depender de la respuesta de la API,
	# no de la carga del archivo JSON.
	def cargar_países_api(self) -> bool:
		'''
		Guarda tasas de cambio desde una API externa
		:return bool: `True` si la API dio respuesta;
		`False` si la comunicación falló.
		'''
		info_países = requests.get(
			f'{os.getenv("url_api_paises")}/country.json'
		).json()

		tasas_cop = requests.get(
			f'{os.getenv("url_api_paises")}/currencies/cop.json'
		).json()["cop"]

		for alfa2 in info_países:
			país = País(
				alfa2,
				info_países[alfa2]['country_name'],
				info_países[alfa2]['currency_code'],
				tasas_cop[info_países[alfa2]['currency_code']]
			)
			self.países[alfa2] = país
		
		fue_guardado = self.guardar_json(self.países, 'países.json')
		return fue_guardado

	def guardar_viaje(self, viaje: Viaje) -> bool:
		'''Guarda un nuevo viaje'''
		self.viajes[viaje.fecha_inicio] = viaje
		
		fue_guardado = self.guardar_json(self.viajes, 'viajes.json')
		return fue_guardado
			
	def guardar_gasto(self, gasto: Gasto) -> bool:
		'''Guarda un gasto asociado a un viaje'''
		pass
			
	def buscar_viaje(self, fecha: date) -> Viaje:
		if fecha in self.países:
			return self.países[fecha]
		
		# Buscamos el viaje que siga vigente en la fecha indicada.
		fecha_anterior = max([f for f in self.viajes if f < fecha])
		if self.viajes[fecha_anterior].get_fecha_fin() > fecha:
			return self.viajes[fecha_anterior]
		
		return None

	def buscar_país(self, alfa2: str) -> País:
		if alfa2 in self.países:
			return self.países[alfa2]
		return None

	def guardar_json(self, entries: dict, filename: str) -> bool:
		try:
			with open(f'{os.getenv("url_data")}/{filename}', 'w') as file:
				json.dump(entries, file, indent=2)
			return True
		except Exception as e:
			print(f"Error al guardar el archivo {filename}: {e}")
			return False