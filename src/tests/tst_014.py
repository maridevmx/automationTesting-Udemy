# -*- coding: utf-8 -*-
#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Modelando funciones Selenium: Conexión a base de datos
# Autor:    M.M.
# Fecha:    11/07/2020
#
# Descripción: Se realizan las configuraciones para los navegadores
#
###############################
# Log:
# 11/07/2020    MMM - Se crea el archivo
################################

from src.functions.Functions import Functions as Selenium
import unittest

class Test_014(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.pyodbc_query(self, "SELECT * FROM BD_SDFT_INS_WEB.PORTAFOLIO")
        print("Se obtienen los portafolios.")
        Selenium.abrir_navegador(self, "https://www.google.com/")
        # CARGAR EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "Google")

    def test_014(self):

        # date = Selenium.textDataEnvironmentReplace(self, "last month")
        # Selenium.get_elements(self, "txt_busqueda").send_keys(date)
        # Selenium.send_especific_keys(self, "txt_busqueda", "Enter")

        pass

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
