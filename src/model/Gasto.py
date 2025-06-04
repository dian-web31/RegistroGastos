import uuid
from datetime import date
from model.TipoGasto import TipoGasto
from model.MedioPago import MedioPago
from model.Viaje import Viaje

class Gasto:
	def __init__(self, fecha: date, valor_cop: float, tipo_gasto: TipoGasto, medio_pago: MedioPago):
		self.id = str(uuid.uuid4())
		self.fecha = fecha
		self.valor_cop = valor_cop
		self.tipo_gasto = tipo_gasto
		self.medio_pago = medio_pago