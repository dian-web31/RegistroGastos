from datetime import date
from src.model.Gasto import Gasto
from model.Pais import Pais

class Viaje:
	def __init__(self, fecha_inicio: date, fecha_fin: date, presupuesto_diario: float, Pais: Pais):
		self.fecha_inicio = fecha_inicio
		self.fecha_fin = fecha_fin
		self.presupuesto_diario = presupuesto_diario
		self.Pais = Pais
		self.gastos: list[Gasto] = []

	def get_fecha_fin(self) -> date:
		return self.fecha_fin

	# Método para calcular el presupuesto total del viaje
	def agregar_gasto(self, gasto):
		self.gastos.append(gasto)
