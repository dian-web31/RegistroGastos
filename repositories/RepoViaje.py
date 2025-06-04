import json
class RepoViaje:
    """
    Repositorio para gestionar viajes y países.
    """
    def __init__(self):
        self.viaje_actual = None  # Objeto de Viaje
        self.paises = []  # Lista de objetos País
        
    def cargar(self) -> bool:
        """Carga datos iniciales desde archivo"""
        try:
            with open("viaje.json", "r") as f:
                data = json.load(f)
                
        except FileNotFoundError:
            self.viaje_actual = None
        
    def cargar_paises_api(self) -> bool:
        """Carga tasas de cambio desde API externa"""
        pass
        
    def guardar_viaje(self, viaje: 'Viaje') -> bool:
        """Guarda un nuevo viaje"""
        if self.viaje_actual:
            with open("viaje.json", "w") as f:
                json.dump(self.viaje_actual.to_dict(), f)
        
    def guardar_gasto(self, gasto: 'Gasto') -> bool:
        """Guarda un gasto asociado a un viaje"""
        pass
        
    def buscar_viaje(self, fecha: date) -> 'Viaje':
        """Busca viaje por fecha de inicio"""
        pass
        
    def buscar_pais(self, codigo: str) -> 'País':
        """Busca país por código"""
        