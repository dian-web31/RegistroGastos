from datetime import date
from src.model.Gasto import Gasto
from src.model.País import País

class Viaje:
	def __init__(self, fecha_inicio: date, fecha_fin: date, presupuesto_diario: float, país: País):
		self.fecha_inicio = fecha_inicio
		self.fecha_fin = fecha_fin
		self.presupuesto_diario = presupuesto_diario
		self.país = país
		self.gastos: list[Gasto] = []

	# Método para calcular el presupuesto total del viaje
	def agregar_gasto(self, gasto):
		self.gastos.append(gasto)
