# -*- coding: utf-8 -*-
#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Modelando funciones Selenium: Assert & Verificaciones
# Autor:    M.M.
# Fecha:    08/07/2020
#
# Descripción: Se realizan las configuraciones para los navegadores
#
###############################
# Log:
# 08/07/2020    MMM - Se crea el archivo
################################

from src.functions.Functions import Functions as Selenium
from src.pages.spotify_registro import Registro
import unittest
import time


class Test_009(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        # CARGAR EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "spotify_registro")

    def test_009(self):

        assert "No coinciden", Selenium.get_text(self, "Titulo") == Registro.tituloPagina
        # assert "No coinciden", Selenium.get_elements(self, "Titulo").text == Registro.tituloPagina

        # Selenium.get_text(self, "Titulo") == Registro.tituloPagina
        Selenium.get_elements(self, "Email").send_keys("34534")
        Selenium.send_especific_keys(self, "Email", "Tab")
        Selenium.assert_text(self, "mensaje_error_email", "Este correo electrónico no es válido. Asegúrate de que tenga un formato como este: ejemplo@email.com")

        time.sleep(5)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
