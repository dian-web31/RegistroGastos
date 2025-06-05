from datetime import date

class País:
	'''
	Modelo de datos para representar un país.
	Los atributos de la clase Pais son recolectados de la Exchange-API.

	GET https://latest.currency-api.pages.dev/v1/currencies/cop.json
	GET https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json
	'''
	def __init__(self, alfa2: str, nombre: str, codigo_divisa:str, tasa_cambio_cop: float, fecha_tasa: date):
		self.alfa2 = alfa2
		self.nombre = nombre
		self.código_divisa = codigo_divisa
		self.tasa_cambio_cop = tasa_cambio_cop
		self.fecha_tasa = fecha_tasa

	def set_tasa_cambio_cop(self, tasa_cambio_cop: float) -> None:
		'''
		Actualiza la tasa de cambio del país.
		:param tasa_cambio_cop: Nueva tasa de cambio en COP.
		'''
		self.tasa_cambio_cop = tasa_cambio_cop
		self.fecha_tasa = date.today()

	def to_json(self) -> dict:
		return {
			'alfa2': self.alfa2,
			'nombre': self.nombre,
			'codigo_divisa': self.código_divisa,
			'tasa_cambio_cop': self.tasa_cambio_cop,
			'fecha_tasa': self.fecha_tasa.isoformat()
		}
	
	@classmethod
	def from_json(cls, json_data: dict) -> 'País':
		"""
		Crea una instancia de País a partir de un diccionario JSON
		:param json_data: Diccionario con los datos del país en formato JSON
		:return: Instancia de País
		"""
		return cls(
			alfa2=json_data['alfa2'],
			nombre=json_data['nombre'],
			codigo_divisa=json_data['codigo_divisa'],
			tasa_cambio_cop=json_data['tasa_cambio_cop'],
			fecha_tasa=date.fromisoformat(json_data['fecha_tasa'])
		)