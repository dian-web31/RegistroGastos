from datetime import date
from src.model.Gasto import Gasto
from src.model.País import País

class Viaje:
	def __init__(
		self,
		fecha_inicio: date,
		fecha_fin: date,
		presupuesto_diario: float,
		país: País
	):
		self.fecha_inicio = fecha_inicio
		self.fecha_fin = fecha_fin
		self.presupuesto_diario = presupuesto_diario
		self.país = país
		self.gastos: list[Gasto] = []

	def get_fecha_fin(self) -> date:
		return self.fecha_fin

	def get_alfa2_país(self) -> str:
		return self.país.alfa2

	def set_tasa_país(self, tasa_cop) -> None:
		self.país.tasa_cambio_cop = tasa_cop

	# Método para calcular el presupuesto total del viaje
	def agregar_gasto(self, gasto):
		self.gastos.append(gasto)

	def to_json(self) -> str:
		return {
			'fecha_inicio': self.fecha_inicio.isoformat(),
			'fecha_fin': self.fecha_fin.isoformat(),
			'presupuesto_diario': self.presupuesto_diario,
			'pais': self.país.to_json(),
			'gastos': [gasto.to_json() for gasto in self.gastos]
		}