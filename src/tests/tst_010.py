import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_010(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def test_010(self):

        # -------------------- INGRESO A LA APP --------------------
        self.driver.get("https://www.mercadolibre.com.mx/")

        # //*[contains(@class,'main-title')]
        # self.LISTADO = self.driver.find_elements_by_xpath("//*[contains(@class,'main-title')]")
        self.PAYMENTS = self.driver.find_elements(By.XPATH, "//*[contains(@class,'payment-data-title')]")

        self.count = 0

        # for self.index, self.lista in enumerate(self.LISTADO):
        #   print(str(self.index) + ".- " + self.lista.text)

        for self.index,self.PAY in enumerate(self.PAYMENTS):
            RESULTADO_ESPERADO = ['Paga en hasta 12 MSI', 'Tarjeta de débito', 'Efectivo, depósito y transferencia', 'Más medios de pago']

            assert RESULTADO_ESPERADO[self.index] == self.PAY.text, "No coinciden"

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
