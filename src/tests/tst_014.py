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
import allure

@allure.feature(u'Test Udemy 1')
@allure.story(u'014: Se visita Google y se coloca una fecha')       # Breve descripción
@allure.testcase(u'Caso de prueba 014')                             # Existe un segundo parámetro para ligarlo a una herramienta como Jira o TestLink
@allure.severity(allure.severity_level.NORMAL)                      # Nivel de severidad del caso de prueba
@allure.description(u"""Se requiere visitar el sitio de Google: </br> 
Deseamos ingresar texto en el recuadro de búsqueda de Google""")
class Test_014(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'Paso 1: Ingresar a Google'):
            Selenium.pyodbc_query(self, "SELECT * FROM BD_SDFT_INS_WEB.PORTAFOLIO")
            print("Se obtienen los portafolios.")
            Selenium.abrir_navegador(self, "https://www.google.com/")
            # CARGAR EL JSON CON LOS VALORES DE LOS ID DE LA APP
            Selenium.get_json_file(self, "Google")

    def test_014(self):
        with allure.step(u'Paso 2: Ingresar término de búsqueda'):
            date = Selenium.textDataEnvironmentReplace(self, "last month")
            Selenium.get_elements(self, "txt_busqueda").send_keys(date)
            Selenium.send_especific_keys(self, "txt_busqueda", "Enter")

    def tearDown(self):
        with allure.step(u'Paso 3: Se cierra el navegador'):
            Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
