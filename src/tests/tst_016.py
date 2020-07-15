# -*- coding: utf-8 -*-
#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Modelando funciones Selenium: Desestimando pruebas en la ejecución
# Autor:    M.M.
# Fecha:    14/07/2020
#
# Descripción: Se realizan las configuraciones para los navegadores
#
###############################
# Log:
# 14/07/2020    MMM - Se crea el archivo
################################

from src.functions.Functions import Functions as Selenium
from src.pages.spotify_registro import Registro
import unittest
import pytest

class Test_016(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        # CARGAR EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "spotify_registro")

    def test_016(self):

        assert "No coinciden", Selenium.get_text(self, "Titulo") == Registro.tituloPagina
        # assert "No coinciden", Selenium.get_elements(self, "Titulo").text == Registro.tituloPagina

        Selenium.get_elements(self, "Email").send_keys(Registro.emailUsuario)
        Selenium.get_elements(self, "emailConfirm").click()

        captcha = Selenium.validar_elemento(self, "Captcha")

        if captcha:
            pytest.skip("No se ejecutó la prueba. La captcha está visible.")

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
