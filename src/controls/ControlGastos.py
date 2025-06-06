from datetime import date
from src.repositories.RepoViajes import RepoViajes
from src.model.Gasto import Gasto
from src.model.TipoGasto import TipoGasto
from src.model.MedioPago import MedioPago

class ControlGastos:
	def __init__(self, repo_viajes: RepoViajes):
		self.repo_viajes = repo_viajes

	def registrar_gasto(self, fecha, valor, tipo, medio):
		viaje = self.repo_viajes.buscar_viaje(fecha)
		if viaje is None:
			raise ValueError(
				'No existe un viaje registrado para la fecha proporcionada.'
			)

		fecha = date.fromisoformat(fecha)

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
		if país.tasa_cambio_cop is None:
			raise ValueError("No hay tasa de cambio disponible para este país")
		
		valor_cop = valor * país.tasa_cambio_cop

		gasto = Gasto(fecha, valor_cop, tipo_gasto, medio_pago)
		self.repo_viajes.guardar_gasto(gasto)

		total_diario = 0
		for gasto in viaje.gastos:
			if gasto.fecha == fecha:
				total_diario += gasto.valor_cop
		
		return viaje.presupuesto_diario - total_diario