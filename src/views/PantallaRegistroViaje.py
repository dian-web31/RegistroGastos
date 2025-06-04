from controls.ControlViajes import ControlViajes

class PantallaRegistroViaje:
	def __init__(self, control_viajes: ControlViajes):
		self.control_viajes = control_viajes

	def registrar_viaje(self) -> None:
		print('\n--- Registro de un viaje ---')

		print('\tCódigo alfa-2 del país')
		alfa2 = input('(puede buscarlo en http://utils.mucattu.com/iso_3166-1.html): ').lower()
		fecha_inicio = input('\tFecha de inicio (YYYY-MM-DD): ')
		fecha_fin = input('\tFecha de finalización (YYYY-MM-DD): ')
		presupuesto_diario = float(input('\tPresupuesto diario (en COP): '))
		
		try:
			viaje = self.control_viajes.registrar_viaje(alfa2, fecha_inicio, fecha_fin, presupuesto_diario)
			print(f'¡Viaje a {viaje.país.nombre} registrado exitosamente!')
			print('Disfrute de su paseo...')
		except ValueError as e:
			print('Error al registrar el viaje. Verifique los datos ingresados.')
			print(f'El error: {e}')