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

		self.cargar()
	
	def cargar(self) -> bool:
		'''
		Carga los datos de países desde `países.json`.

		En primera instancia, se intenta cargar los países desde la API.
		Se mantiene una copia estructurada de esta en el JSON.
		- API: https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json.

		:return bool: `True` si se cargó la información contenida en los JSON;
		`False` si el contenido JSON es inválido.
		'''
		try:
			api_cargada = self.cargar_países_api()
			if not api_cargada:
				self.cargar_json('países.json')
			self.cargar_json('viajes.json')
			return True
		except Exception as e:
			print(e)
			return False

	# TODO - El retorno debe depender de la respuesta de la API,
	# no de la carga del archivo JSON.
	def cargar_países_api(self) -> bool:
		'''
		Carga en memoria todos los países desde una API externa
		y guarda una copia en `países.json`.

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
			tasa_cop = None
			if info_países[alfa2]['currency_code'] in tasas_cop:
				tasa_cop = tasas_cop[info_países[alfa2]['currency_code']]
			
			país = País(
				alfa2,
				info_países[alfa2]['country_name'],
				info_países[alfa2]['currency_code'],
				tasa_cop
			)
			self.países[alfa2] = país
		
		países_json = [p.to_json() for p in self.países.values()]
		fue_guardado = self.guardar_json(países_json, 'países.json')
		return fue_guardado

	def guardar_viaje(self, viaje: Viaje) -> bool:
		'''
		:return bool: `True` si el viaje fue guardado correctamente;
		`False` si ya existe un viaje durante la fecha.
		'''
		viaje_existente = self.buscar_viaje(viaje.fecha_inicio)
		
		if viaje_existente is not None:
			self.viajes[viaje.fecha_inicio] = viaje
			
			viajes_json = [v.to_json() for v in self.viajes.values()]
			self.guardar_json(viajes_json, 'viajes.json')
			
			return True
		return False
			
	def guardar_gasto(self, gasto: Gasto) -> bool:
		'''
		:return bool: `True` si el gasto fue guardado correctamente;
		`False` si no existe un viaje correspondiente a la fecha.
		'''
		gasto_existente = self.buscar_viaje(gasto.fecha)
		
		if gasto_existente is not None:
			self.viajes[gasto.fecha] = gasto
			
			viajes_json = [v.to_json() for v in self.viajes.values()]
			self.guardar_json(viajes_json, 'viajes.json')
			
			return True
		return False
			
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

	def cargar_json(self, filename: str) -> dict:
		try:
			with open(f'{os.getenv("url_data")}/{filename}', 'r') as file:
				return json.load(file)
		except Exception as e:
			print(f"Error al cargar el archivo {filename}: {e}")
			return {}