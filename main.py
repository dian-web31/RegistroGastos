from src.views.PantallaReportes import PantallaReportes
from src.views.PantallaRegistroGasto import PantallaRegistroGasto
from src.views.PantallaRegistroViaje import PantallaRegistroViaje

def main(self):
	self.opciones = {
		'Registrar viaje': PantallaRegistroViaje.registrar_viaje,
		'Registrar gasto': PantallaRegistroGasto.registrar_gasto,
		'Ver reportes por día': PantallaReportes.mostrar_reporte_diario,
		'Ver reportes por tipo de gasto': PantallaReportes.mostrar_reporte_tipo_gasto
	}

	while True:
		print('\n--- Sistema de registro de expensas ---')
		for index, description in enumerate(self.opciones.keys()):
			print(f'{index + 1}: {description}')
		print('0. Salir')

		opción = int(input('Seleccione una opción: '))
		if opción == 0:
			print('¡Hasta luego!')
			break

		if opción <= len(self.opciones):
			enumerate(self.opciones.values())
		else:
			print('Opción inválida, intente nuevamente.')

if __name__ == '__main__':
	main()
