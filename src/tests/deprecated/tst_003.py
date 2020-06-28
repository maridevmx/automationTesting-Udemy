import unittest
import pytest

class Test_003(unittest.TestCase):

    def setUp(self):
        pass

    def test_comparacion(self):
        self.Variable_A = 51
        self.Variable_B = 50

    def test_004(self):
        self.Variable_A = 2

        if self.Variable_A < 3:
            unittest.TestCase.skipTest(self, "El valor es muy inferior para ejecutar la prueba")

        if self.Variable_A >= 10:
            self.RESULTADO = True

        else:
            self.RESULTADO = False

        assert self.RESULTADO, f"El valor no es mayor, es: {self.Variable_A}"

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()