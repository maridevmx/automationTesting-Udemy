# -*- coding: utf-8 -*-
#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Modelando funciones Selenium: Screenshots
# Autor:    M.M.
# Fecha:    13/07/2020
#
# Descripción: Se realizan las configuraciones para obtener capturas de pantalla
#
###############################
# Log:
# 13/07/2020    MMM - Se crea el archivo
################################

from src.functions.Functions import Functions as Selenium
import unittest
import allure

@allure.feature(u'Test Udemy 1')
@allure.story(u'015: Se realiza la captura de pantalla')            # Breve descripción
@allure.testcase(u'Caso de prueba 015')                             # Existe un segundo parámetro para ligarlo a una herramienta como Jira o TestLink
@allure.severity(allure.severity_level.NORMAL)                      # Nivel de severidad del caso de prueba
@allure.description(u"""Se requiere visitar el sitio de Google: </br> 
Deseamos ingresar texto en el recuadro de búsqueda de Google""")

class Test_015(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'Paso 1: Ingresar a Google'):
            Selenium.abrir_navegador(self, "https://www.google.com/")
            # CARGAR EL JSON CON LOS VALORES DE LOS ID DE LA APP
            Selenium.get_json_file(self, "Google")

    def test_015(self):
        with allure.step(u'Paso 2: Se realiza captura de pantalla'):
            path = Selenium.captura(self, "Google")
            Selenium.esperar(self, 5)

    def tearDown(self):
        with allure.step(u'Paso 3: Se cierra el navegador'):
            Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
