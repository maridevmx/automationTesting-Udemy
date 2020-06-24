import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Capturas de pantalla con Selenium
# Autor:    M.M. Mena
# Fecha:    15/06/2020
#
# Descripción: Uso de la función get_screenshot_as_file para capturar la
# pantalla de prueba
#
###############################
# Log:
# 15/06/2020    MMM - Se crea el archivo
################################

horaGlobal = time.strftime("%H%M%S")

class Test_015(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

        # -------------------- INGRESO A LA APP --------------------
        self.driver.get("https://www.amazon.com.mx/")

    def test_015(self):
        localizador = self.driver.find_element(By.XPATH,
                                               "/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
        self.driver.execute_script("arguments[0].click();", localizador)
        time.sleep(5)

        title = "Amazon.com.mx Mensaje"
        assert title == self.driver.title, "No son iguales"

        self.driver.get_screenshot_as_file(f"../data/capturas/{title}-{horaGlobal}.png")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
