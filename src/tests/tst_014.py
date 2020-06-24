import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Selenium Keys
# Autor:    M.M. Mena
# Fecha:    15/06/2020
#
# Descripción: Uso de la función sendKeys para enviar comandos como si se
# escribiera con el teclado
#
###############################
# Log:
# 15/06/2020    MMM - Se crea el archivo
################################

class Test_014(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

        # -------------------- INGRESO A LA APP --------------------
        self.driver.get("https://www.google.com/")

    def test_014(self):

        self.driver.find_element(By.XPATH,"//input[@name='q']").send_keys("Curso de Selenium en Udemy")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.ENTER)
        time.sleep(2)



    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
