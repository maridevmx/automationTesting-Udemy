# -*- coding: utf-8 -*-
#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Modelando funciones Selenium: JavaScript
# Autor:    M.M.
# Fecha:    07/07/2020
#
# Descripción: Se realizan la configuración con las funcionas ya modeladas
#
###############################
# Log:
# 07/07/2020    MMM - Se crea el archivo
################################

from src.functions.Functions import Functions as Selenium
import unittest

class Test_006(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.amazon.com.mx/")

    def test_006(self):
        # CARGAR EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "Amazon")
        Selenium.scroll_to(self, "Liga Amazon")
        Selenium.esperar(5)
        Selenium.js_clic(self, "Liga Amazon")
        Selenium.page_has_loaded(self)
        Selenium.esperar(5)

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
