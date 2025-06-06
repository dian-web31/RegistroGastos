from datetime import date
from src.model.Gasto import Gasto
from src.model.País import País
from src.model.JSONSerializable import JSONSerializable

class Viaje(JSONSerializable):
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
	
	@classmethod
	def from_json(cls, json_data: dict) -> 'Viaje':
		"""
		Crea una instancia de Viaje a partir de un diccionario JSON
		:param json_data: Diccionario con los datos del viaje en formato JSON
		:return: Instancia de Viaje
		"""
		viaje = cls(
			fecha_inicio=date.fromisoformat(json_data['fecha_inicio']),
			fecha_fin=date.fromisoformat(json_data['fecha_fin']),
			presupuesto_diario=json_data['presupuesto_diario'],
			país=País.from_json(json_data['pais'])
		)
		
		# Reconstruir los gastos si existen
		if 'gastos' in json_data:
			for gasto_json in json_data['gastos']:
				viaje.agregar_gasto(Gasto.from_json(gasto_json))
		
		return viaje