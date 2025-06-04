import uuid
from datetime import date
from src.model.TipoGasto import TipoGasto
from src.model.MedioPago import MedioPago

class Gasto:
	def __init__(self, fecha: date, valor_cop: float, tipo_gasto: TipoGasto, medio_pago: MedioPago):
		self.id = str(uuid.uuid4())
		self.fecha = fecha
		self.valor_cop = valor_cop
		self.tipo_gasto = tipo_gasto
		self.medio_pago = medio_pago
	
	def to_json(self) -> dict:
		return {
			'id': self.id,
			'fecha': self.fecha.isoformat(),
			'valor_cop': self.valor_cop,
			'tipo_gasto': self.tipo_gasto.name(),
			'medio_pago': self.medio_pago.name()
		}