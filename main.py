# main.py

from controls.ControlViajes import ControlViajes
from controls.ControlGastos import ControlGastos
from controls.ControlReportes import ControlReportes
from repositories.RepoViaje import RepoViaje
from datetime import date

def main():
    repo = RepoViaje()
    repo.cargar()
    repo.cargar_paises_api()

    control_viajes = ControlViajes(repo)
    control_gastos = ControlGastos(repo)
    control_reportes = ControlReportes(repo)

    while True:
        print("\n--- Sistema de Registro de Gastos de Viaje ---")
        print("1. Registrar viaje")
        print("2. Registrar gasto")
        print("3. Ver reporte de gastos diarios")
        print("4. Ver reporte de gastos por tipo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo_pais = input("Código ISO del país: ").upper()
            fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
            presupuesto_diario = float(input("Presupuesto diario (COP): "))

            viaje = control_viajes.registrar_viaje(
                codigo_pais=codigo_pais,
                fecha_inicio=date.fromisoformat(fecha_inicio),
                fecha_fin=date.fromisoformat(fecha_fin),
                presupuesto_diario=presupuesto_diario
            )
            if viaje:
                print("✔ Viaje registrado correctamente.")
            else:
                print("✘ No se pudo registrar el viaje.")

        elif opcion == "2":
            fecha = input("Fecha del gasto (YYYY-MM-DD): ")
            valor = float(input("Valor del gasto: "))
            tipo = int(input("Tipo de gasto (0: Transporte, 1: Alojamiento, 2: Alimentación, 3: Entretenimiento, 4: Compras): "))
            medio = int(input("Medio de pago (1: Efectivo, 2: Tarjeta): "))

            valor_cop = control_gastos.registrar_gasto(
                fecha=date.fromisoformat(fecha),
                valor=valor,
                tipo=tipo,
                medio=medio
            )
            print(f"✔ Gasto registrado en COP: {valor_cop:.2f}")

        elif opcion == "3":
            fecha_inicio = input("Fecha inicio del viaje (YYYY-MM-DD): ")
            reporte = control_reportes.reportar_gastos_diarios(date.fromisoformat(fecha_inicio))

            print("\nGastos diarios:")
            for fecha, monto in reporte.items():
                print(f"{fecha}: ${monto:.2f} COP")

        elif opcion == "4":
            fecha_inicio = input("Fecha inicio del viaje (YYYY-MM-DD): ")
            reporte = control_reportes.reportar_gastos_por_tipo(date.fromisoformat(fecha_inicio))

            print("\nGastos por tipo:")
            for fecha, tipos in reporte.items():
                print(f"{fecha}:")
                for tipo, valor in tipos.items():
                    print(f"  {tipo}: ${valor:.2f} COP")

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()
