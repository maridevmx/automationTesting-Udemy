import unittest

class Test_002(unittest.TestCase):

    def setUp(self):
        pass

    def test_002(self):
        self.Variable_A = 50
        self.Variable_B = 50
        self.RESULTADO = self.Variable_A + self.Variable_B

        self.assertEqual(self.Variable_A, self.Variable_B, "Los valores son distintos")

    def test_003(self):
        self.Variable_A = 40
        self.Variable_B = 50
        self.RESULTADO = self.Variable_A + self.Variable_B

        self.assertNotEqual(self.Variable_A, self.Variable_B, "Los valores son distintos")

    def test_004(self):
        self.Variable_A = 10

        if self.Variable_A >= 10:
            self.RESULTADO = True

        else:
            self.RESULTADO = False

        self.assertTrue(self.RESULTADO, f"El valor no es verdadero, es: {self.Variable_A}")

    def test_005(self):
        self.Variable_A = "Bienvenido a la clase de unittest"
        self.Variable_B = "Bienvenido"

        self.assertIn(self.Variable_B, self.Variable_A, f"No coinciden")

    def test_006(self):
        self.Variable_A = "Bienvenido a la clase de unittest"
        self.Variable_B = "Hola"

        self.assertIsNot(self.Variable_B, self.Variable_A, f"No coinciden")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
