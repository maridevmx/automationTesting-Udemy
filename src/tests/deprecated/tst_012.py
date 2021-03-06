import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Selenium JavaScript Execute - Click()
# Autor:    M.M.
# Fecha:    15/06/2020
#
# Descripción: Uso de la función de JavaScript - Click() en la aplicación
# de Amazon
#
###############################
# Log:
# 15/06/2020    MMM - Se crea el archivo
################################

class Test_012(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

        # -------------------- INGRESO A LA APP --------------------
        self.driver.get("https://www.amazon.com.mx/")

    def test_012(self):

        time.sleep(5)
        localizador = self.driver.find_element(By.XPATH,"//a[@id='nav-hamburger-menu']")
        self.driver.execute_script("arguments[0].click();", localizador)

        time.sleep(5)
        localizador = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
        self.driver.execute_script("arguments[0].click();", localizador)
        time.sleep(5)

        assert "Amazon.com.mx Mensaje" == self.driver.title, "No son iguales"
    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
