# -*- coding: utf-8 -*-
#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Modelando funciones Selenium: Variables de escenario
# Autor:    M.M.
# Fecha:    09/07/2020
#
# Descripción: Se realizan las configuraciones para los navegadores
#
###############################
# Log:
# 09/07/2020    MMM - Se crea el archivo
################################

from src.functions.Functions import Functions as Selenium
from src.pages.spotify_registro import Registro
import unittest
import time


class Test_012(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        # CARGAR EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "spotify_registro")

    def test_012(self):

        assert "No coinciden", Selenium.get_text(self, "Titulo") == Registro.tituloPagina
        # assert "No coinciden", Selenium.get_elements(self, "Titulo").text == Registro.tituloPagina

        # Selenium.get_text(self, "Titulo") == Registro.tituloPagina
        Selenium.save_variable_scenary(self, "verifica_cuenta", "Variable_verifica")

        Selenium.new_window(self, "https://www.spotify.com/mx/signup/")

        Selenium.switch_to_windows_name(self, "Spotify_registro")

        Selenium.compare_with_variable_scenary(self, "verifica_cuenta", "Variable_verifica")

        Selenium.esperar(self, 3)

        # RECUPERAR DESDE EXCEL
        NOMBRE = Selenium.leer_celda(self, "A1")
        APELLIDO = Selenium.leer_celda(self, "B1")
        DNI = Selenium.leer_celda(self, "C1")

        Selenium.create_variable_scenary(self, "NOMBRE", NOMBRE)
        Selenium.create_variable_scenary(self, "APELLIDO", APELLIDO)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
