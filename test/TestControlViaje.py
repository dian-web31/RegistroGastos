import unittest
from unittest.mock import MagicMock, patch
from datetime import date, timedelta
from src.controls.ControlViajes import ControlViajes
from src.model.País import País
from src.repositories.RepoViajes import RepoViajes

class TestControlViajes(unittest.TestCase):
    def setUp(self):
        # Configuración común para todas las pruebas
        self.repo_mock = MagicMock(spec=RepoViajes)
        self.control_viajes = ControlViajes(self.repo_mock)

        # Configurar un país de prueba
        self.pais_test = País("co", "Colombia", "cop", 1.0, date.today())

    def test_registro_viaje_exitoso(self):
        """Prueba que un viaje se registre correctamente con datos válidos"""
        # Configurar mocks
        self.repo_mock.buscar_país.return_value = self.pais_test
        self.repo_mock.guardar_viaje.return_value = True

        # Datos de prueba
        alfa2 = "co"
        fecha_inicio = (date.today() + timedelta(days=1)).isoformat()  # Mañana
        fecha_fin = (date.today() + timedelta(days=8)).isoformat()     # En una semana
        presupuesto = 150000.0

        # Ejecutar
        viaje = self.control_viajes.registrar_viaje(alfa2, fecha_inicio, fecha_fin, presupuesto)

        # Verificar
        self.repo_mock.guardar_viaje.assert_called_once()
        self.assertEqual(viaje.país.nombre, "Colombia")
        self.assertEqual(viaje.presupuesto_diario, presupuesto)
        self.assertEqual(viaje.fecha_inicio, date.fromisoformat(fecha_inicio))
        self.assertEqual(viaje.fecha_fin, date.fromisoformat(fecha_fin))

    def test_registro_viaje_fecha_pasada(self):
        """Prueba que falle al intentar registrar viaje con fecha en el pasado"""
        # Datos de prueba con fecha en el pasado
        fecha_inicio = (date.today() - timedelta(days=1)).isoformat()
        fecha_fin = date.today().isoformat()

        # Verificar que lanza excepción
        with self.assertRaises(ValueError) as context:
            self.control_viajes.registrar_viaje("co", fecha_inicio, fecha_fin, 100000)

        self.assertIn("no puede ser anterior a la fecha actual", str(context.exception))
        self.repo_mock.guardar_viaje.assert_not_called()

    def test_registro_viaje_fechas_invertidas(self):
        """Prueba que falle cuando fecha fin es anterior a fecha inicio"""
        # Datos de prueba con fechas invertidas
        fecha_inicio = (date.today() + timedelta(days=2)).isoformat()
        fecha_fin = (date.today() + timedelta(days=1)).isoformat()

        # Verificar que lanza excepción
        with self.assertRaises(ValueError) as context:
            self.control_viajes.registrar_viaje("co", fecha_inicio, fecha_fin, 100000)

        self.assertIn("debe ser posterior a la fecha de inicio", str(context.exception))
        self.repo_mock.guardar_viaje.assert_not_called()

    def test_registro_viaje_pais_inexistente(self):
        """Prueba que falle cuando el país no existe"""
        # Configurar mock para simular país no encontrado
        self.repo_mock.buscar_país.return_value = None

        # Datos de prueba válidos excepto por el país
        fecha_inicio = (date.today() + timedelta(days=1)).isoformat()
        fecha_fin = (date.today() + timedelta(days=8)).isoformat()

        # Verificar que lanza excepción
        with self.assertRaises(ValueError) as context:
            self.control_viajes.registrar_viaje("xx", fecha_inicio, fecha_fin, 100000)

        self.assertIn("No se encontró un país", str(context.exception))
        self.repo_mock.guardar_viaje.assert_not_called()

    def test_registro_viaje_fecha_ocupada(self):
        """Prueba que falle cuando ya existe un viaje para la fecha de inicio"""
        # Configurar mocks
        self.repo_mock.buscar_país.return_value = self.pais_test
        self.repo_mock.guardar_viaje.return_value = False  # Simula que ya existe

        # Datos de prueba válidos
        fecha_inicio = (date.today() + timedelta(days=1)).isoformat()
        fecha_fin = (date.today() + timedelta(days=8)).isoformat()

        # Verificar que lanza excepción
        with self.assertRaises(ValueError) as context:
            self.control_viajes.registrar_viaje("co", fecha_inicio, fecha_fin, 100000)

        self.assertIn("Ya existe un viaje registrado", str(context.exception))
        self.repo_mock.guardar_viaje.assert_called_once()

