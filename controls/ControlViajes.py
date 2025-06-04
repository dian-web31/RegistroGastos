from models.Viaje import Viaje

class ControlViajes:
    def __init__(self, repo):
        self.repo = repo

    def registrar_viaje(self, codigo_pais, fecha_inicio, fecha_fin, presupuesto_diario):
        pais = self.repo.buscar_pais(codigo_pais)
        viaje = Viaje(fecha_inicio, fecha_fin, presupuesto_diario, pais)
        self.repo.viajes[fecha_inicio] = viaje
        self.repo.guardar_viaje(viaje.__dict__)
        return viaje

    def buscar_viaje(self, fecha_inicio):
        return self.repo.buscar_viaje(fecha_inicio)