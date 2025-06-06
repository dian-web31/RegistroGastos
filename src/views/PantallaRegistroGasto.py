from src.controls.ControlGastos import ControlGastos
from src.model.MedioPago import MedioPago
from src.model.TipoGasto import TipoGasto

class PantallaRegistroGasto:
	def __init__(self, control_gastos: ControlGastos):
		self.control_gastos = control_gastos

	def registrar_gasto(self) -> None:
		print('\n--- Registro de un gasto ---')

		fecha = input('Fecha (YYYY-MM-DD): ')
		valor = float(input('Valor del gasto en moneda local: '))
		print('Tipos de gasto:')
		for tipo in TipoGasto:
			print(f'\t{tipo.value} - {tipo.name}')
		tipo = int(input('Seleccione un tipo: '))
		print('Medios de pago:')
		for medio in MedioPago:
			print(f'\t{medio.value} - {medio.name}')
		medio = int(input('Seleccione un medio: '))
		print()

		try:
			diferencia = self.control_gastos.registrar_gasto(fecha, valor, tipo, medio)
			print('¡Gasto registrado exitosamente!')
			print(f'Presupuesto restante del día: {diferencia}')
		except ValueError as e:
			print('Error al registrar el gasto. Verifique los datos ingresados.')
			print(f'El error: {e}')