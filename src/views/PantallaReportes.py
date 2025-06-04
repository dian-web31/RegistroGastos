class PantallaReportes:
    def __init__(self, controlador):
        self.controlador = controlador

    def mostrar_reportes(self):
        fecha_inicio = input("Fecha de inicio del viaje (YYYY-MM-DD): ")
        diarios = self.controlador.reportar_gastos_diarios(fecha_inicio)
        por_tipo = self.controlador.reportar_gastos_por_tipo(fecha_inicio)

        print("\n📊 Gastos diarios:")
        for fecha, valor in diarios.items():
            print(f"{fecha}: ${valor:.2f} COP")

        print("\n📊 Gastos por tipo:")
        for tipo, valor in por_tipo.items():
            print(f"{tipo}: ${valor:.2f} COP")
