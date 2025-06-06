import unittest
from unittest.mock import MagicMock, patch
from datetime import date, timedelta
from src.controls.ControlGastos import ControlGastos
from src.model.TipoGasto import TipoGasto
from src.model.MedioPago import MedioPago
from src.model.País import País
from src.model.Viaje import Viaje
from src.repositories.RepoViajes import RepoViajes

class TestControlGastos(unittest.TestCase):
    def setUp(self):
        # Configuración común para todas las pruebas
        self.repo_mock = MagicMock(spec=RepoViajes)
        self.control_gastos = ControlGastos(self.repo_mock)

        # Configurar un país de prueba
        self.pais_test = País("co", "Colombia", "cop", 1.0, date.today())

        # Configurar un viaje de prueba
        hoy = date.today()
        self.viaje_test = Viaje(hoy, hoy + timedelta(days=7), 100000, self.pais_test)

    def test_registro_gasto_exitoso_cop(self):
        """Prueba que un gasto en COP se registre correctamente"""
        # Configurar mocks
        self.repo_mock.buscar_viaje.return_value = self.viaje_test
        self.repo_mock.buscar_país.return_value = self.pais_test

        # agregar el gasto a la lista del viaje.
        def guardar_gasto_side_effect(gasto):
            self.viaje_test.agregar_gasto(gasto)  # Usando el método del modelo Viaje

        self.repo_mock.guardar_gasto.side_effect = guardar_gasto_side_effect

        # Datos de prueba
        fecha = date.today().isoformat()
        valor = 50000
        tipo = TipoGasto.ALIMENTACION.value
        medio = MedioPago.TARJETA.value

        # Ejecutar
        diferencia = self.control_gastos.registrar_gasto(fecha, valor, tipo, medio)

        # Verificar
        self.repo_mock.guardar_gasto.assert_called_once()
        self.assertEqual(diferencia, 50000)  # 100000 - 50000
        gasto_guardado = self.repo_mock.guardar_gasto.call_args[0][0]
        self.assertEqual(gasto_guardado.valor_cop, 50000)
        self.assertEqual(gasto_guardado.tipo_gasto, TipoGasto.ALIMENTACION)

    def test_registro_gasto_exitoso_divisa_extranjera(self):
        """Prueba que un gasto en moneda extranjera se convierta correctamente a COP"""
        # Configurar país con tasa de cambio
        pais_usa = País("us", "Estados Unidos", "usd", 3800, date.today())
        viaje_usa = Viaje(date.today(), date.today() + timedelta(days=7), 1000000, pais_usa)

        # Configurar mocks
        self.repo_mock.buscar_viaje.return_value = viaje_usa
        self.repo_mock.buscar_país.return_value = pais_usa

        # Esta función simula que el gasto se agrega a la lista del viaje a USA.
        def guardar_gasto_side_effect(gasto):
            viaje_usa.agregar_gasto(gasto)

        # Le asignamos el efecto secundario al mock.
        self.repo_mock.guardar_gasto.side_effect = guardar_gasto_side_effect

        # Datos de prueba (50 USD)
        fecha = date.today().isoformat()
        valor = 50
        tipo = TipoGasto.ENTRETENIMIENTO.value
        medio = MedioPago.EFECTIVO.value

        # Ejecutar
        diferencia = self.control_gastos.registrar_gasto(fecha, valor, tipo, medio)

        # Verificar
        gasto_guardado = self.repo_mock.guardar_gasto.call_args[0][0]
        self.assertEqual(gasto_guardado.valor_cop, 190000)  # 50 * 3800
        self.assertAlmostEqual(diferencia, 810000)  # 1,000,000 - 190,000

    def test_registro_gasto_sin_viaje(self):
        """Prueba que falle al intentar registrar gasto sin viaje existente"""
        # Configurar mock para simular que no hay viaje
        self.repo_mock.buscar_viaje.return_value = None

        # Datos de prueba
        fecha = date.today().isoformat()
        valor = 50000
        tipo = TipoGasto.TRANSPORTE.value
        medio = MedioPago.TARJETA.value

        # Verificar que lanza excepción
        with self.assertRaises(ValueError) as context:
            self.control_gastos.registrar_gasto(fecha, valor, tipo, medio)

        self.assertIn("No existe un viaje registrado", str(context.exception))
        self.repo_mock.guardar_gasto.assert_not_called()

    # test/TestControlGasto.py

    def test_registro_gasto_tipo_invalido(self):
        """Prueba que se lance un ValueError al registrar un gasto con tipo inválido"""
        # Configurar mocks (solo se necesita buscar_viaje, ya que fallará antes)
        self.repo_mock.buscar_viaje.return_value = self.viaje_test

        # Datos de prueba con tipo inválido
        fecha = date.today().isoformat()
        valor = 50000
        tipo_invalido = 99  # Tipo que no existe
        medio = MedioPago.EFECTIVO.value

        # --- FORMA CORRECTA DE PROBAR EXCEPCIONES ---
        # Este bloque "with" espera que el código dentro de él lance un ValueError.
        # Si lo hace, la prueba PASA. Si no lo hace (o lanza otra excepción), la prueba FALLA.
        with self.assertRaises(ValueError) as context:
            self.control_gastos.registrar_gasto(fecha, valor, tipo_invalido, medio)

        # Opcional: Verificar que el mensaje de la excepción es el esperado.
        self.assertIn("Tipo de gasto inválido", str(context.exception))

        # Verificar que el gasto NUNCA se intentó guardar, porque la función
        # se detuvo antes.
        self.repo_mock.guardar_gasto.assert_not_called()
    def test_registro_gasto_sin_tasa_cambio(self):
        """Prueba que falle al intentar registrar gasto sin tasa de cambio"""
        # Configurar país sin tasa de cambio
        pais_sin_tasa = País("eu", "Unión Europea", "EUR", None, date.today())
        viaje_eu = Viaje(date.today(), date.today() + timedelta(days=7), 100000, pais_sin_tasa)

        # Configurar mocks
        self.repo_mock.buscar_viaje.return_value = viaje_eu
        self.repo_mock.buscar_país.return_value = pais_sin_tasa
        # Datos de prueba
        fecha = date.today().isoformat()
        valor = 50  # EUR
        tipo = TipoGasto.COMPRAS.value
        medio = MedioPago.TARJETA.value
        # Verificar que lanza excepción
        with self.assertRaises(ValueError) as context:
            self.control_gastos.registrar_gasto(fecha, valor, tipo, medio)

        self.assertIn("No hay tasa de cambio disponible", str(context.exception))
        self.repo_mock.guardar_gasto.assert_not_called()