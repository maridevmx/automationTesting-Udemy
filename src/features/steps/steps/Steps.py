# -*- coding: utf-8 -*-
from behave import *
import pytest
import unittest
from selenium.webdriver.common.keys import Keys
from functions.Functions import Functions as Selenium
from functions.Inicializar import Inicializar

use_step_matcher("re")

class StepsDefinitions():

    @given("Abrir la aplicacion")
    def step_impl(self):
        Selenium.abrir_navegador(self)
        Selenium.page_has_loaded(self)


    @given("Inicializo la app en la URL (.*)")
    def step_impl(self, URL):
        Selenium.abrir_navegador(self, URL = URL )


    @given("Abro la app con el navegador (.*)")
    def step_impl(self, navegador):
        Selenium.abrir_navegador(self, NAVEGADOR = navegador)


    @then("Cierro la app")
    def step_impl(self):
        Selenium.tearDown(self)


    @given("Cargo el DOM de la App: (.*)")
    def step_impl(self, file):
        Selenium.get_json_file(self, FILE = file)


    @step("En el campo (.*) se escribe (.*)")
    def step_impl(self, entity, text):
        Selenium.send_key_text(self, entity, text)


    @step("Se captura pantalla: (.*)")
    def step_impl(self, descripcion):
        Selenium.captura(self, descripcion)


    @step("Se toma captura de pantalla (.*)")
    def step_impl(self, testCase):
        Selenium.capturar_pantalla(self, testCase)


    @step("En el dropdown (.*) se selecciona (.*)")
    def step_impl(self, locator, text):
        Selenium.select_by_text(self, locator, text)


    @step("Se realiza un desplazamiento al frame: (.*)")
    def step_impl(self, frame):
        Selenium.switch_to_iframe(self, frame)


    @step("Se regresa al Frame Padre")
    def step_impl(self):
        Selenium.switch_to_parentFrame(self)


    @step("Se realiza un click en (.*)")
    def step_impl(self, locator):
        Selenium.get_elements(self, locator).click()


    @step("Se realiza clic en el texto: (.*)")
    def step_impl(self, Text):
        Selenium.get_elements(self, "text", MyTextElement = Text).click()


    @step("Se realiza un scroll hacia el elemento: (.*)")
    def step_impl(self, locator):
        Selenium.scroll_to(self, locator)


    @step("Esperar que finalice la carga de la pagina")
    def step_impl(self):
        Selenium.page_has_loaded(self)