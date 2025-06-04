import json
from models.Viaje import Viaje
from models.Gasto import Gasto
from models.Pais import Pais

class RepoViaje:
    def __init__(self):
        self.viajes = {}  # dict[date, Viaje]
        self.paises = {}  # dict[str, Pais]

    def cargar(self):
        # Suponiendo que hay archivos JSON persistidos localmente
        try:
            with open("data/viajes.json", "r") as f:
                viajes_data = json.load(f)
                # Parseo omitido por brevedad
            return True
        except:
            return False

    def cargar_paises_api(self):
        # Aquí se llamaría a la API externa para llenar self.paises
        return True

    def guardar_viaje(self, json_viaje):
        # Aquí se serializa un viaje y se guarda en JSON
        return True

    def guardar_gasto(self, json_gasto):
        # Guardar el gasto en la lista correspondiente
        return True

    def buscar_viaje(self, fecha):
        return self.viajes.get(fecha)

    def buscar_pais(self, codigo):
        return self.paises.get(codigo)
