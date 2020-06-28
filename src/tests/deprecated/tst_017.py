import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Construcción de XPATH
# Autor:    M.M.
# Fecha:    16/06/2020
#
# Descripción: Uso de XPATH en el registro de la aplicación de Spotify
#
###############################
# Log:
# 16/06/2020    MMM - Se crea el archivo
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
        Posicion = 1
        Text = {"pruebaTest17@gmail.com", "pruebaTest17@gmail.com", "MiPass2020", "Prueba17Udemy"}

        while(Posicion <= 4):
            self.driver.find_element(By.XPATH,u"(//*[@required])" + "[" + str(Posicion) + "]").send_keys(Text[Posicion-1])
            Posicion = Posicion + 1

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
