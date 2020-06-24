import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Uso de ActionChains
# Autor:    M.M. Mena
# Fecha:    15/06/2020
#
# Descripción: Usos de la función ActionChains en la aplicación
# de MercadoLibre
#
###############################
# Log:
# 15/06/2020    MMM - Se crea el archivo
################################

class Test_011(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

        # -------------------- INGRESO A LA APP --------------------
        self.driver.get("https://www.mercadolibre.com.mx/")

    def test_011(self):

        localizador = self.driver.find_element(By.XPATH,
                                               "/html[1]/body[1]/header[1]/div[1]/div[2]/ul[1]/li[2]/a[1]")
        action = ActionChains(self.driver)

        action.move_to_element(localizador)
        action.perform()

        localizador2 = self.driver.find_element(By.XPATH,
                                                "/html[1]/body[1]/header[1]/div[1]/div[2]/ul[1]/li[2]/nav[1]/section[1]/ul[2]/li[1]/a[1]")
        action.move_to_element(localizador2)
        action.perform()

        time.sleep(5)

        localizador3 = self.driver.find_element(By.XPATH,
                                                "/html[1]/body[1]/header[1]/div[1]/div[2]/ul[1]/li[2]/nav[1]/section[2]/div[1]/div[1]/article[1]/h2[1]/a[1]")
        localizador3.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
