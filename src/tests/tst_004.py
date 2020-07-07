# -*- coding: utf-8 -*-
#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Modelando funciones Selenium: Switch entre Iframes y ventanas
# Autor:    M.M.
# Fecha:    06/07/2020
#
# Descripción: Se realizan la configuración con las funcionas ya modeladas
#
###############################
# Log:
# 06/07/2020    MMM - Se crea el archivo
################################

from src.functions.Functions import Functions as Selenium
from src.pages.spotify_registro import Registro
import unittest
import time


class Test_004(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://chercher.tech/practice/frames-example-selenium-webdriver")

    def test_004(self):

        # CARGAR EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "frames")

        # -------------------- IR A FRAME 2 --------------------
        Selenium.switch_to_iframe(self, "Frame2")
        Selenium.select_by_text(self, "Frame2 Select", "Avatar")
        time.sleep(5)

        # -------------------- VOLVER AL FRAME PRINCIPAL --------------------
        Selenium.switch_to_parentFrame(self)

        # -------------------- IR A FRAME 1 --------------------
        Selenium.switch_to_iframe(self, "Frame1")
        Selenium.send_key_text(self, "Frame1 Input", "Hola Chicos Udemy")
        time.sleep(5)

        # -------------------- IR A FRAME 3 --------------------
        Selenium.switch_to_iframe(self, "Frame3")
        Selenium.get_elements(self, "Frame3 Input").click()


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
