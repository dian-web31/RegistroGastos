from src.repositories.RepoViajes import RepoViajes

class ControlReportes:
	def __init__(self, repo_viajes: RepoViajes):
		self.repo_viajes = repo_viajes

	def reportar_gastos_diarios(self, fecha):
		viaje = self.repo_viajes.buscar_viaje(fecha)
		
		reporte = {}
		for gasto in viaje.gastos:
			reporte.setdefault(gasto.fecha, 0)
			reporte[gasto.fecha] += gasto.valor_cop
		return reporte

	def reportar_gastos_por_tipo(self, fecha):
		viaje = self.repo_viajes.buscar_viaje(fecha)
		
		reporte = {}
		for gasto in viaje.gastos:
			tipo = gasto.tipo_gasto.name.title()
			reporte.setdefault(tipo, 0)
			reporte[tipo] += gasto.valor_cop
		return reporte