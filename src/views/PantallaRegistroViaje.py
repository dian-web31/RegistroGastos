from src.controls.ControlViajes import ControlViajes

class PantallaRegistroViaje:
	def __init__(self, control_viajes: ControlViajes):
		self.control_viajes = control_viajes

	def registrar_viaje(self) -> None:
		print('\n--- Registro de un viaje ---')

		print('Código alfa-2 del país (puede buscarlo en http://utils.mucattu.com/iso_3166-1.html)')
		alfa2 = input('> ').lower()
		fecha_inicio = input('Fecha de inicio (YYYY-MM-DD): ')
		fecha_fin = input('Fecha de finalización (YYYY-MM-DD): ')
		presupuesto_diario = float(input('Presupuesto diario (en COP): '))
		
		try:
			viaje = self.control_viajes.registrar_viaje(alfa2, fecha_inicio, fecha_fin, presupuesto_diario)
			print(f'¡Viaje a {viaje.país.nombre} registrado exitosamente!')
			print('Disfrute de su paseo...')
		except ValueError as e:
			print('Error al registrar el viaje. Verifique los datos ingresados.')
			print(f'El error: {e}')