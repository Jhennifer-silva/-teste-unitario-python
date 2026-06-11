import unittest

from calculadora import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    potencia,
    calcular_media,
)


class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        casos = [
            (2, 3, 5),
            (5, 0, 5),
            (0, 0, 0),
            (-2, 5, 3),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(somar(a, b), esperado)

    def test_subtrair(self):
        casos = [
            (10, 5, 5),
            (5, 10, -5),
            (0, 0, 0),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(subtrair(a, b), esperado)

    def test_multiplicar(self):
        casos = [
            (3, 4, 12),
            (5, 0, 0),
            (-2, 3, -6),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(multiplicar(a, b), esperado)

    def test_dividir(self):
        casos = [
            (10, 2, 5.0),
            (5, 2, 2.5),
            (0, 5, 0.0),
            (-10, 2, -5.0),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(dividir(a, b), esperado)

    def test_dividir_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_potencia(self):
        casos = [
            (2, 3, 8),
            (5, 0, 1),
            (10, 2, 100),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(potencia(a, b), esperado)

    def test_calcular_media(self):
        casos = [
            ([10, 8, 6], 8),
            ([2.5, 7.5], 5.0),
            ([10], 10),
        ]

        for lista, esperado in casos:
            with self.subTest(lista=lista):
                self.assertEqual(calcular_media(lista), esperado)

    def test_calcular_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])


if __name__ == "__main__":
    unittest.main()