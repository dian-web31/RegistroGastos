from controls.ControlViajes import ControlViajes
from model.MedioPago import MedioPago
from model.TipoGasto import TipoGasto

class PantallaRegistroGasto:
	def __init__(self, control_gastos: ControlViajes):
		self.control_gastos = control_gastos

	def registrar_gasto(self) -> None:
		print('\n--- Registro de un gasto ---')

		fecha = input('\tFecha (YYYY-MM-DD): ')
		valor = float(input('\tValor del gasto en moneda local: '))
		print('\tTipos de gasto:')
		for tipo in TipoGasto:
			print(f'\t\t{tipo.value} - {tipo.name}')
		tipo = int(input('\tSeleccione un tipo: '))
		print('Medios de pago:')
		for medio in MedioPago:
			print(f'\t\t{medio.value} - {medio.name}')
		medio = int(input('\tSeleccione un medio: '))

		try:
			diferencia = self.control_gastos.registrar_gasto(fecha, valor, tipo, medio)
			print('¡Gasto registrado exitosamente!')
			print(f'Presupuesto restante del día: {diferencia}')
		except ValueError as e:
			print('Error al registrar el gasto. Verifique los datos ingresados.')
			print(f'El error: {e}')