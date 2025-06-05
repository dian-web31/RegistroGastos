"""
Implementacion del repositorio para la persistencia de viajes y gastos.
"""
import json
import os
from datetime import date
import requests
from dotenv import load_dotenv
from src.model.Gasto import Gasto
from src.model.Pais import Pais
from src.model.Viaje import Viaje
load_dotenv()

class RepoViajes:
    """
	Este repositorio gestiona viajes y sus respectivos gastos,
	además de mantener una copia local de los Paises que se recuperan de la API.
	"""
    def __init__(self):
        self.viajes: dict[date, Viaje] = {}
        self.Paises: dict[str, Pais] = {}
    def cargar(self) -> bool:
        """
		Carga los datos del modelo desde los archivos JSON.\n
		En primera instancia, se intenta cargar los Paises desde la API \
		https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json.
		Se mantiene una copia estructurada de la información en `Paises.json`.\n
		:return bool: `True` si se cargó la información contenida en los JSON;			
		`False` si los archivos JSON son inválidos.
		"""
        try:
            with open('viaje.json', 'r') as f:
                data = json.load(f)				
        except FileNotFoundError:
            self.viaje_actual = None

		# TODO - El retorno debe depender de la respuesta de la API,
		# no de la carga del archivo JSON.
        def cargar_Paises_api(self) -> bool:
            '''
			Guarda tasas de cambio desde una API externa
			:return bool: `True` si la API dio respuesta;
			`False` si la comunicación falló.
			'''
            info_Paises = requests.get(
				f"{os.getenv('url_api_paises')}/country.json"
			).json()

            tasas_cop = requests.get(
				f"{os.getenv('url_api_paises')}/currencies/cop.json"
			).json()["cop"]

            for alfa2 in info_Paises:
                Pais = Pais(
					alfa2,
					info_Paises[alfa2]['country_name'],
					info_Paises[alfa2]['currency_code'],
					tasas_cop[info_Paises[alfa2]['currency_code']]
				)
                self.Paises[alfa2] = Pais
            fue_guardado = self.guardar_json(self.Paises, 'Paises.json')
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
            if fecha in self.Paises:
                return self.Paises[fecha]
			# Buscamos el viaje que siga vigente en la fecha indicada.
            fecha_anterior = max([f for f in self.viajes if f < fecha])
            if self.viajes[fecha_anterior].get_fecha_fin() > fecha:
                return self.viajes[fecha_anterior]
            return None

        def buscar_Pais(self, alfa2: str) -> Pais:
            if alfa2 in self.Paises:
                return self.Paises[alfa2]
            return None

        def guardar_json(self, entries: dict, filename: str) -> bool:
            try:
                with open(f"{os.getenv('url_data')}/{filename}", 'w') as file:
                    json.dump(entries, file, indent=2)
                return True
            except Exception as e:
                print(f"Error al guardar el archivo {filename}: {e}")
                return False
            