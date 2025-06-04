"""
Modelo de datos para representar un país.
Los atributos de la clase Pais son recolectados de la Exchange-API.

GET https://latest.currency-api.pages.dev/v1/currencies/cop.json
GET https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json
"""
class Pais:
    def __init__(self, codigo: str, nombre: str, tasa_cambio_cop: float):
        self.codigo = codigo
        self.nombre = nombre
        self.tasa_cambio_cop = tasa_cambio_cop
