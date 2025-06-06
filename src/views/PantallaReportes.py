from src.controls.ControlReportes import ControlReportes

class PantallaReportes:
	def __init__(self, control_reportes: ControlReportes):
		self.control_reportes = control_reportes

	def mostrar_reporte_diario(self):
		print('\n--- Reporte de gastos por día ---')

		fecha = input('Fecha en la que estuvo en el viaje (YYYY-MM-DD): ')
		print()

		reporte = self.control_reportes.reportar_gastos_diarios(fecha)
		print('Los gastos hechos por día en el viaje fueron:')
		for fecha, valor in reporte.items():
			print(f'{fecha}: ${valor:.2f} COP')

	def mostrar_reporte_tipo(self):
		print('\n--- Reporte de gastos por tipo de gasto ---')

		fecha = input('Fecha en la que estuvo en el viaje (YYYY-MM-DD): ')
		print()

		reporte = self.control_reportes.reportar_gastos_por_tipo(fecha)
		print('Los gastos hechos por concepto o tipo en el viaje fueron:')
		for tipo, valor in reporte.items():
			valor = f'{valor:.2f}'
			print(f'- {tipo + ":" :<20} {"$" + valor + " COP" :>20}')
