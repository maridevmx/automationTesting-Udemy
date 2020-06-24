import unittest


class Test_001(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 4
        self.Variable_B = 6

    def test_001(self):
        self.Resultado = self.Variable_A + self.Variable_B

    def tearDown(self):
        self.assertTrue(self.Resultado == 10, f"El valor no es 10, es {self.Resultado}")

if __name__ == '__main__':
    unittest.main()
