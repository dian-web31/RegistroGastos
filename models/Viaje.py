from datetime import date
from models.Pais import Pais

"""
Clase Viaje que representa un viaje con sus detalles y gastos asociados.
"""
class Viaje:
    def __init__(self, fecha_inicio: date, fecha_fin: date, presupuesto_diario: float, pais: Pais):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.presupuesto_diario = presupuesto_diario
        self.pais = pais
        self.gastos = []  # lista de objetos Gasto

    # Método para calcular el presupuesto total del viaje
    def agregar_gasto(self, gasto):
        self.gastos.append(gasto)
