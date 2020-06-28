import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Uso de localizadores de elementos
# Autor:    M.M. Mena
# Fecha:    16/06/2020
#
# Descripción: Uso de XPATH en el registro de la aplicación de Spotify
#
###############################
# Log:
# 16/06/2020    MMM - Se crea el archivo
################################

horaGlobal = time.strftime("%H%M%S")

class Test_016(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

        # -------------------- INGRESO A LA APP --------------------
        self.driver.get("https://www.spotify.com/mx/signup/")
        time.sleep(5)

    def test_016(self):
        self.driver.find_element(By.NAME, "email").send_keys("pruebaTest16@gmail.com")
        time.sleep(5)

        self.driver.find_element(By.ID, "confirm").send_keys("pruebaTest16@gmail.com")
        time.sleep(5)

        self.driver.find_element(By.CSS_SELECTOR, "div.signuppage__Signup-sof6g5-0.YsCoj:nth-child(4) form:nth-child(4) div.Group-sc-1lird8m-0.iNEHpO:nth-child(8) label.Checkbox-sc-1141y94-0.fRKYyx > span.Indicator-sc-11vkltc-0.hrjscC")
        time.sleep(5)

        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Condiciones de Uso").click()

        title = "Registrarte - Spotify"
        assert title == self.driver.title, "No son iguales"

        self.driver.get_screenshot_as_file(f"../data/capturas/{title}-{horaGlobal}.png")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
