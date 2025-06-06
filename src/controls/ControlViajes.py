from datetime import date
from src.model.Viaje import Viaje
from src.repositories.RepoViajes import RepoViajes

# TODO - Every date has to be in the same timezone,
# so we can compare them correctly (both in Viajes and Gastos).
# We can use the Colombia timezone as focus,
# and import the `pytz` library to handle timezones;
# we can also consume an API to get the timezone of the country
# where the trip is being made, then convert all dates to GMT-5:00.

class ControlViajes:
	def __init__(self, repo_viajes: RepoViajes):
		self.repo = repo_viajes
			
	def registrar_viaje(self,
		alfa2: str,
		fecha_inicio: str,
		fecha_fin: str,
		presupuesto_diario: float
	) -> Viaje:
		fecha_inicio = date.fromisoformat(fecha_inicio)
		if fecha_inicio < date.today():
			raise ValueError(
				'La fecha de inicio no puede ser anterior a la fecha actual'
			)
		
		fecha_fin = date.fromisoformat(fecha_fin)
		if fecha_inicio >= fecha_fin:
			raise ValueError(
				'La fecha de finalización debe ser posterior a la fecha de inicio'
			)
			
		país = self.repo.buscar_país(alfa2)
		if not país:
			raise ValueError(
				'No se encontró un país con el código alfa-2 proporcionado'
			)
		
		viaje = Viaje(fecha_inicio, fecha_fin, presupuesto_diario, país)
		
		fue_guardado = self.repo.guardar_viaje(viaje)
		if not fue_guardado:
			raise ValueError(
				'Ya existe un viaje registrado para la fecha de inicio proporcionada'
			)
		
		return viaje
			
	def buscar_viaje(self, fecha_inicio: date) -> Viaje:
		return self.repo.buscar_viaje(fecha_inicio)