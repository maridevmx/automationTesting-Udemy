# -*- coding: utf-8 -*-
#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Modelando funciones Selenium: Identificadores
# Autor:    M.M.
# Fecha:    29/06/2020
#
# Descripción: Se realizan las configuraciones para los navegadores
#
###############################
# Log:
# 29/06/2020    MMM - Se crea el archivo
################################

from src.functions.Functions import Functions as Selenium
from src.pages.spotify_registro import Registro
import unittest
import time


class Test_003(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_003(self):

        # CARGAR EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "spotify_registro")

        # ACCEDER A LAS KEYS (ENTIDADES) DEL JSON
        #Selenium.get_entity(self, "Titulo")

        assert "No coinciden", Selenium.get_text(self, "Titulo") == Registro.tituloPagina
        # assert "No coinciden", Selenium.get_elements(self, "Titulo").text == Registro.tituloPagina

        # Selenium.get_text(self, "Titulo") == Registro.tituloPagina

        Selenium.esperar_elemento(self, "Email")

        Selenium.esperar_elemento(self, "emailConfirm")

        Selenium.get_elements(self, "Email").send_keys(Registro.emailUsuario)
        Selenium.get_elements(self, "emailConfirm").send_keys(Registro.emailUsuarioConfirm)
        Selenium.get_elements(self, "Password").send_keys(Registro.passwordUsuario)
        Selenium.get_elements(self, "Perfil").send_keys(Registro.aliasUsuario)

        Selenium.get_select_element(self, "Mes de nacimiento").select_by_visible_text("Enero")

        time.sleep(5)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
