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

class Test_007(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")

    def test_007(self):
        # CARGAR EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "frames")
        Selenium.switch_to_iframe(self, "Frame4 Alerta")
        Selenium.get_elements(self, "Alerta").click()
        Selenium.esperar(5)
        Selenium.alert_windows(self, "accept")
        Selenium.esperar(5)

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
