from models.Gasto import Gasto
from models.TipoGasto import TipoGasto
from models.MedioPago import MedioPago

class ControlGastos:
    def __init__(self, repo):
        self.repo = repo

    def convertir_cop(self, codigo_divisa: str, valor: float):
        pais = self.repo.buscar_pais(codigo_divisa)
        return valor * pais.tasa_cambio_cop

    def registrar_gasto(self, fecha, valor, tipo, medio, viaje):
        tipo_enum = TipoGasto(tipo)
        medio_enum = MedioPago(medio)
        valor_cop = self.convertir_cop(viaje.pais.codigo, valor)
        gasto = Gasto(fecha, valor_cop, tipo_enum, medio_enum, viaje)
        viaje.agregar_gasto(gasto)
        self.repo.guardar_gasto(gasto.__dict__)
        return gasto