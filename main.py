from views.PantallaReportes import PantallaReportes
from views.PantallaRegistroGasto import PantallaRegistroGasto
from views.PantallaRegistroViaje import PantallaRegistroViaje

def main():
    while True:
        print('\n--- Sistema de Registro de Gastos de Viaje ---')
        print('1. Registrar viaje')
        print('2. Registrar gasto')
        print('3. Ver reporte de gastos')
        print('4. Salir')

        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            PantallaRegistroViaje.registrar_viaje()

        elif opcion == '2':
            PantallaRegistroGasto.registrar_gasto()

        elif opcion == '3':
            PantallaReportes.mostrar_reportes()

        elif opcion == '4':
            print('¡Hasta luego!')
            break

        else:
            print('Opción inválida, intente nuevamente.')

if __name__ == '__main__':
    main()
