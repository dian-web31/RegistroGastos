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
			'tipo_gasto': self.tipo_gasto.name,
			'medio_pago': self.medio_pago.name
		}
	
	@classmethod
	def from_json(cls, json_data: dict) -> 'Gasto':
		"""
		Crea una instancia de Gasto a partir de un diccionario JSON
		
		Args:
			json_data: Diccionario con los datos del gasto en formato JSON
			
		Returns:
			Instancia de Gasto reconstruida
			
		Raises:
			ValueError: Si faltan campos requeridos o hay formatos inválidos
		"""
		try:
			# Validar campos requeridos
			required_fields = ['id', 'fecha', 'valor_cop', 'tipo_gasto', 'medio_pago']
			if not all(field in json_data for field in required_fields):
				raise ValueError("Faltan campos requeridos en los datos del gasto")
			
			# Convertir enum strings de vuelta a los tipos enum
			tipo_gasto = TipoGasto[json_data['tipo_gasto']]
			medio_pago = MedioPago[json_data['medio_pago']]
			
			# Crear instancia
			gasto = cls(
				fecha=date.fromisoformat(json_data['fecha']),
				valor_cop=float(json_data['valor_cop']),
				tipo_gasto=tipo_gasto,
				medio_pago=medio_pago
			)
			
			# Restaurar el ID original (el constructor genera uno nuevo)
			gasto.id = json_data['id']
			
			return gasto
			
		except KeyError as e:
			raise ValueError(f"Valor de enumeración inválido: {str(e)}") from e
		except ValueError as e:
			raise ValueError(f"Error en formato de datos: {str(e)}") from e