class PantallaRegistroGasto:
    def __init__(self, controlador):
        self.controlador = controlador

    def registrar_gasto(self):
        fecha = input("Fecha (YYYY-MM-DD): ")
        valor = float(input("Valor en moneda local: "))
        tipo = int(input("Tipo de gasto [1-5]: "))
        medio = int(input("Medio de pago [1=Efectivo, 2=Tarjeta]: "))
        fecha_inicio = input("Fecha inicio del viaje: ")
        viaje = self.controlador.repo.buscar_viaje(fecha_inicio)
        self.controlador.registrar_gasto(fecha, valor, tipo, medio, viaje)
        print("✔️ Gasto registrado")