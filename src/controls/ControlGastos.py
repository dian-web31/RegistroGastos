from src.controls import ControlViajes
from src.repositories.RepoViajes import RepoViajes
from src.model.Gasto import Gasto
from src.model.TipoGasto import TipoGasto
from src.model.MedioPago import MedioPago

class ControlGastos:
	def __init__(self, repo_viajes: RepoViajes):
		self.repo_viajes = repo_viajes

	def convertir_cop(self, codigo_divisa: str, valor: float):
		país = self.repo_viajes.buscar_país(codigo_divisa)
		return valor * país.tasa_cambio_cop

	def registrar_gasto(self, fecha, valor, tipo, medio):
		viaje = self.repo_viajes.buscar_viaje(fecha)
		if viaje is None:
			raise ValueError(
				'No existe un viaje registrado para la fecha proporcionada.'
			)

		try:
			tipo_gasto = TipoGasto(tipo)
		except ValueError:
			print(
				'Tipo de gasto inválido. ',
				f'Se esperaba un número entre 1 y {len(TipoGasto)}.'
			)
		
		try:
			medio_pago = MedioPago(medio)
		except ValueError:
			print(
				'Medio de pago inválido. ',
				f'Se esperaba un número entre 1 y {len(MedioPago)}.'
			)
		
		país = self.repo_viajes.buscar_país(viaje.get_alfa2_país())
		valor_cop = self.convertir_cop(viaje.get_alfa2_país(), valor)

		gasto = Gasto(fecha, valor_cop, tipo_gasto, medio_pago, viaje)
		viaje.agregar_gasto(gasto)
		self.repo_viajes.guardar_gasto(gasto.__dict__)
		return gasto