from src.repositories.RepoViajes import RepoViajes
from src.model.Gasto import Gasto
from src.model.TipoGasto import TipoGasto
from src.model.MedioPago import MedioPago

class ControlGastos:
	def __init__(self, repo_viajes: RepoViajes):
		self.repo = repo_viajes

	def convertir_cop(self, codigo_divisa: str, valor: float):
		Pais = self.repo.buscar_Pais(codigo_divisa)
		return valor * Pais.tasa_cambio_cop

	def registrar_gasto(self, fecha, valor, tipo, medio, viaje):
		tipo_enum = TipoGasto(tipo)
		medio_enum = MedioPago(medio)
		valor_cop = self.convertir_cop(viaje.Pais.codigo, valor)
		gasto = Gasto(fecha, valor_cop, tipo_enum, medio_enum, viaje)
		viaje.agregar_gasto(gasto)
		self.repo.guardar_gasto(gasto.__dict__)
		return gasto