from models.Viaje import Viaje
from repositories.RepoViaje import RepoViaje

class ControlViajes:
    def __init__(self, repositorio: RepoViaje):
        self.repo = repositorio
        
    def registrar_viaje(self, codigo_pais, fecha_inicio, 
                       fecha_fin, presupuesto_diario) -> Viaje:
        """Registra un nuevo viaje con validaciones"""
        if fecha_inicio >= fecha_fin:
            raise ValueError("Fecha fin debe ser posterior a fecha inicio")
            
        pais = self.repo.buscar_pais(codigo_pais)
        if not pais:
            raise ValueError("País no encontrado")
            
        viaje = Viaje(fecha_inicio, fecha_fin, presupuesto_diario, pais)
        self.repo.guardar_viaje(viaje)
        return viaje
        
    def buscar_viaje(self, fecha_inicio: date) -> Viaje:
        """Busca viaje activo por fecha"""
        return self.repo.buscar_viaje(fecha_inicio)