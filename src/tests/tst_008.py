# -*- coding: utf-8 -*-
#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Modelando funciones Selenium: Alerts & Keys
# Autor:    M.M.
# Fecha:    08/07/2020
#
# Descripción: Se realizan la configuración con las funcionas ya modeladas
#
###############################
# Log:
# 08/07/2020    MMM - Se crea el archivo
################################

from src.functions.Functions import Functions as Selenium
import unittest

class Test_008(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.google.com.mx/")
        Selenium.get_json_file(self, "Google")

    def test_008(self):
        Selenium.page_has_loaded(self)
        Selenium.get_elements(self, "txt_busqueda").click()
        Selenium.send_key_text(self, "txt_busqueda", "w3schools")
        Selenium.send_especific_keys(self, "txt_busqueda", "Enter")
        Selenium.esperar(5)

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
