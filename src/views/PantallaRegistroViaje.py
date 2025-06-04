from controls.ControlViajes import ControlViajes

class PantallaRegistroViaje:
    def registrar_viaje():
        """Interfaz para registrar nuevo viaje"""
        print("\n--- Registrar Nuevo Viaje ---")
        codigo_pais = input("Código de país (CO para Colombia): ").upper()
        fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
        fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
        presupuesto = float(input("Presupuesto diario en COP: "))
        
        try:
            viaje = ControlViajes.registrar_viaje(codigo_pais, 
                                                (fecha_inicio), 
                                                (fecha_fin), 
                                                presupuesto)
            print(f"Viaje a {viaje.pais.nombre} registrado exitosamente!")
        except ValueError as e:
            print(f"Error: {e}")