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


class Test_005(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.mercadolibre.com.mx/")

    def test_005(self):

        Selenium.new_window(self, "https://www.mercadolibre.com.mx/ofertas#nav-header")
        time.sleep(3)

        Selenium.switch_to_windows_name(self, "Ofertas")
        time.sleep(3)

        Selenium.switch_to_windows_name(self, "Principal")
        time.sleep(3)

        Selenium.switch_to_windows_name(self, "Ofertas")
        time.sleep(3)

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
