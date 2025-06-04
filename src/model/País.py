class País:
	'''
	Modelo de datos para representar un país.
	Los atributos de la clase Pais son recolectados de la Exchange-API.

	GET https://latest.currency-api.pages.dev/v1/currencies/cop.json
	GET https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json
	'''
	def __init__(self, alfa2: str, nombre: str, codigo_divisa:str, tasa_cambio_cop: float):
		self.alfa2 = alfa2
		self.nombre = nombre
		self.codigo_divisa = codigo_divisa
		self.tasa_cambio_cop = tasa_cambio_cop

	def to_json(self) -> dict:
		return {
			'alfa2': self.alfa2,
			'nombre': self.nombre,
			'codigo_divisa': self.codigo_divisa,
			'tasa_cambio_cop': self.tasa_cambio_cop
		}