from src.repositories.RepoViajes import RepoViajes
from src.controls.ControlReportes import ControlReportes
from src.controls.ControlViajes import ControlViajes
from src.controls.ControlGastos import ControlGastos
from src.views.PantallaReportes import PantallaReportes
from src.views.PantallaRegistroGasto import PantallaRegistroGasto
from src.views.PantallaRegistroViaje import PantallaRegistroViaje

def main(self):
	self.repo_viajes = RepoViajes()

	self.control_viajes = ControlViajes(self.repo_viajes)
	self.control_gastos = ControlGastos(self.repo_viajes, self.control_viajes)
	self.control_reportes = ControlReportes(self.repo_viajes)

	self.pantalla_viajes = PantallaRegistroViaje(self.control_viajes)
	self.pantalla_gastos = PantallaRegistroGasto(self.control_gastos)
	self.pantalla_reportes = PantallaReportes(self.control_reportes)
	
	self.opciones = {
		'Registrar viaje': self.pantalla_viajes.registrar_viaje,
		'Registrar gasto': self.pantalla_gastos.registrar_gasto,
		'Ver reportes por día': self.pantalla_reportes.mostrar_reporte_diario,
		'Ver reportes por tipo de gasto': self.pantalla_reportes.mostrar_reporte_tipo
	}

	while True:
		print('\n--- Sistema de registro de expensas ---')
		for index, description in enumerate(self.opciones.keys()):
			print(f'{index + 1}: {description}')
		print('0. Salir')

		opción = int(input('Seleccione una opción: '))
		# Las opciones negativas que no tienen sentido
		# se consideran como condición de salida del programa.
		if opción <= 0:
			print('¡Hasta luego!')
			break

		if opción <= len(self.opciones):
			# Ejecuta la función que corresponde a la opción - 1
			# en el diccionario self.opciones.
			enumerate(self.opciones.values())[opción - 1]()
		else:
			print('Opción inválida, intente nuevamente.')

if __name__ == '__main__':
	main()
