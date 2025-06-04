from enum import Enum

"""
Clase que representa los gastos en el viaje
"""
class TipoGasto(Enum):
    TRANSPORTE = 1
    ALOJAMIENTO = 2
    ALIMENTACION = 3
    ENTRETENIMIENTO = 4
    COMPRAS = 5