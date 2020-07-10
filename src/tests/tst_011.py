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


class Test_011(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        # CARGAR EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "spotify_registro")

    def test_011(self):

        assert "No coinciden", Selenium.get_text(self, "Titulo") == Registro.tituloPagina
        # assert "No coinciden", Selenium.get_elements(self, "Titulo").text == Registro.tituloPagina

        # Selenium.get_text(self, "Titulo") == Registro.tituloPagina
        Selenium.save_variable_scenary(self, "verifica_cuenta", "verifica_cuenta")
        Selenium.save_variable_scenary(self, "Titulo", "Titulo")

        Selenium.new_window(self, "https://www.google.com/")
        Selenium.get_json_file(self, "Google")

        Selenium.switch_to_windows_name(self, "Google")

        texto = Selenium.get_variable_scenary(self, "verifica_cuenta")

        Selenium.get_elements(self, "txt_busqueda").send_keys(texto)
        Selenium.esperar(self, 10)

        time.sleep(3)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
