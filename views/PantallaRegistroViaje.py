class PantallaRegistroViaje:
    def __init__(self, controlador):
        self.controlador = controlador

    def registrar_viaje(self):
        codigo_pais = input("Código ISO del país: ")
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
        presupuesto_diario = float(input("Presupuesto diario en COP: "))
        self.controlador.registrar_viaje(codigo_pais, fecha_inicio, fecha_fin, presupuesto_diario)
        print("🌍 Viaje registrado")