# -*- coding: utf-8 -*-
#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Configuración de navegadores para Selenium
# Autor:    M.M.
# Fecha:    26/06/2020
#
# Descripción: Se realizan las configuraciones para los navegadores
#
###############################
# Log:
# 26/06/2020    MMM - Se crea el archivo
################################

from src.functions.Functions import Functions as Selenium
from src.pages.spotify_registro import Registro
import unittest


class Test_001(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_001(self):
        # print("Valor del título: " + Registro.lbl_titulo_xpath )
        assert Selenium.xpath_element(self,
                                      Registro.lbl_titulo_xpath).text == "Registrarte con tu correo electrónico", "No coinciden"
        Selenium.xpath_element(self, Registro.txt_email_xpath).send_keys(Registro.emailUsuario)
        Selenium.xpath_element(self, Registro.txt_email_confirm_xpath).send_keys(Registro.emailUsuarioConfirm)

        Selenium._id_element(self,
                            Registro.txt_password_id).send_keys(Registro.passwordUsuario)
        Selenium.id_element(self, Registro.txt_user_id).send_keys(Registro.aliasUsuario)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
