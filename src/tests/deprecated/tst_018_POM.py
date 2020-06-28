import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.spotify_registro import Registro as Spotify_registro

#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Uso de plugins
# Autor:    M.M.
# Fecha:    18/06/2020
#
# Descripción: Uso de XPATH con plugins en el registro de la aplicación de Spotify
#
###############################
# Log:
# 18/06/2020    MMM - Se crea el archivo
################################

horaGlobal = time.strftime("%H%M%S")

class Test_017(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

        # -------------------- INGRESO A LA APP --------------------
        self.driver.get("https://www.spotify.com/mx/signup/")
        time.sleep(5)

    def test_017(self):

        # EMAIL DE USUARIO
        self.driver.find_element(By.XPATH, Spotify_registro.txt_email_xpath).clear()
        self.driver.find_element(By.XPATH, Spotify_registro.txt_email_xpath).send_keys("test18Spotify@gmail.com")

        # CONFIRMACION DE EMAIL
        self.driver.find_element_by_xpath(Spotify_registro.txt_email_confirm_xpath).clear()
        self.driver.find_element_by_xpath(Spotify_registro.txt_email_confirm_xpath).send_keys("test18Spotify@gmail.com")

        title = "Registrarte - Spotify"
        assert title == self.driver.title, "No son iguales"

        self.driver.get_screenshot_as_file(f"../data/capturas/{title}-{horaGlobal}.png")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
