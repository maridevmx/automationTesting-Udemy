import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Test_009(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def test_009(self):

        # -------------------- INGRESO A LA APP --------------------
        self.driver.get("https://autos.mercadolibre.com.mx/sedan/#VEHICLE_BODY_TYPE")

        # //*[contains(@class,'main-title')]
        # self.LISTADO = self.driver.find_elements_by_xpath("//*[contains(@class,'main-title')]")
        self.LISTADO = self.driver.find_elements(By.XPATH, "//*[contains(@class,'main-title')]")
        self.LISTADO2 = self.driver.find_elements(By.XPATH, "//*[contains(@class,'item__attrs')]")
        print("Listado de elementos encontrados: " + str(self.LISTADO.__len__()))

        self.count = 0

        # for self.lista in self.LISTADO:
        for self.index, self.lista in enumerate(self.LISTADO):
            print(str(self.index) + ".- " + self.lista.text)

        for self.LISTA2 in self.LISTADO2:
            print("Características: " + self.LISTA2.text)

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
