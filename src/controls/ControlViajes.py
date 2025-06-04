from datetime import date
from controls.ControlGastos import ControlGastos
from model.Viaje import Viaje
from repositories.RepoViajes import RepoViajes

class ControlViajes:
	def __init__(self, repo_viajes: RepoViajes, control_gastos: ControlGastos):
		self.repo = repo_viajes
		self.control_gastos = control_gastos
			
	def registrar_viaje(self,
		codigo_país,
		fecha_inicio,
		fecha_fin,
		presupuesto_diario
	) -> Viaje:
		if fecha_inicio >= fecha_fin:
			raise ValueError(
				'La fecha de finalización debe ser posterior a la fecha de inicio'
			)
			
		país = self.repo.buscar_país(codigo_país)
		if not país:
			raise ValueError(
				'No se encontró un país con el código alfa-2 proporcionado'
			)
		
		viaje = Viaje(fecha_inicio, fecha_fin, presupuesto_diario, país)
		self.repo.guardar_viaje(viaje)
		return viaje
			
	def buscar_viaje(self, fecha_inicio: date) -> Viaje:
		return self.repo.buscar_viaje(fecha_inicio)