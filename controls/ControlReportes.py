class ControlReportes:
    def __init__(self, repo):
        self.repo = repo

    def reportar_gastos_diarios(self, fecha_inicio):
        viaje = self.repo.buscar_viaje(fecha_inicio)
        resultado = {}
        for gasto in viaje.gastos:
            resultado.setdefault(gasto.fecha, 0)
            resultado[gasto.fecha] += gasto.valor_cop
        return resultado

    def reportar_gastos_por_tipo(self, fecha_inicio):
        viaje = self.repo.buscar_viaje(fecha_inicio)
        resultado = {}
        for gasto in viaje.gastos:
            tipo = gasto.tipo_gasto.name
            resultado.setdefault(tipo, 0)
            resultado[tipo] += gasto.valor_cop
        return resultado