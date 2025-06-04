import uuid
from datetime import date
from models.TipoGasto import TipoGasto
from models.MedioPago import MedioPago

class Gasto:
    def __init__(self, fecha: date, valor_cop: float, tipo_gasto: TipoGasto, medio_pago: MedioPago, viaje):
        self.id = str(uuid.uuid4())
        self.fecha = fecha
        self.valor_cop = valor_cop
        self.tipo_gasto = tipo_gasto
        self.medio_pago = medio_pago
        self.viaje = viaje  # objeto de tipo Viaje
