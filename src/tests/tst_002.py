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
import unittest


class Test_002(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_002(self):
        pass

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
