# -*- coding: utf-8 -*-
#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Configuración de navegadores para Selenium
# Autor:    M.M.
# Fecha:    25/06/2020
#
# Descripción: Se realizan las configuraciones para los navegadores
#
###############################
# Log:
# 25/06/2020    MMM - Se crea el archivo
################################
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.functions.Inicializar import Inicializar
from selenium import webdriver
from selenium.webdriver.ie.options import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as OptionsChrome
import json

class Functions(Inicializar):
    ##########################################################
    ################### INICIALIZAR DRIVERS ##################
    ##########################################################
    def abrir_navegador(self, URL = Inicializar.URL, NAVEGADOR = Inicializar.Navegador):
        print("Directorio base: " + Inicializar.baseDir)
        self.ventanas = {}
        print('--------------------')
        print(NAVEGADOR)
        print('--------------------')

        if NAVEGADOR == ('IExplorer'):
            caps = DesiredCapabilities.INTERNETEXPLORER.copy()
            caps["platform"] = "WINDOWS"
            caps["browserName"] = "internet explorer"
            caps["ignoreZoomSettings"] = True
            caps["requireWindowsFocus"] = True
            caps["nativeEvents"] = True
            self.driver = webdriver.Ie(Inicializar.baseDir + "\\drivers\\IEDriverServer.exe",caps)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal':self.driver.window_handles[0]}
            print(self.ventanas)
            self.nWindows = 0
            return self.driver

        elif NAVEGADOR == ('CHROME'):
            options = OptionsChrome()
            options.add_argument('start-maximized')
            self.driver = webdriver.Chrome(chrome_options = options,
                                           executable_path = Inicializar.baseDir + "\\drivers\\chromedriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal':self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        elif NAVEGADOR == ('FIREFOX'):
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

    def tearDown(self):
        print("Se cerrará el driver")
        self.driver.quit()

    ##########################################################
    ###############  <--- LOCATORS HANDLE --->  ##############
    ##########################################################

    # FUNCIÓN QUE BUSCA ELEMENTOS POR XPATH
    def xpath_element(self, XPATH):
        elements = self.driver.find_element_by_xpath(XPATH)
        print("Xpath Elements: Se interactuó con el elemento " + XPATH)
        return elements

    # FUNCIÓN QUE BUSCA ELEMENTOS POR XPATH
    def _xpath_element(self, XPATH):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
            elements = self.driver.find_element_by_xpath(XPATH)
            print(u"Esperar elemento: Se visualizó el elmento " + XPATH)
            return elements
        except TimeoutException:
            print(u"Esperar Elemento: No presente " + XPATH)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar Elemento: No presente " + XPATH)
            Functions.tearDown(self)

    # FUNCIÓN QUE BUSCA ELEMENTOS POR ID
    def id_element(self, ID):
        elements = self.driver.find_element_by_id(ID)
        print("Id Elements: Se interactuó con el elemento " + ID)
        return elements

    # FUNCIÓN QUE BUSCA ELEMENTOS POR ID
    def _id_element(self, ID):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.ID, ID)))
            elements = self.driver.find_element_by_id(ID)
            print(u"Esperar elemento: Se visualizó el elmento " + ID)
            return elements
        except TimeoutException:
            print(u"Esperar Elemento: No presente " + ID)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar Elemento: No presente " + ID)
            Functions.tearDown(self)

    # AGREGAR FUNCIONES PARA BUSCAR POR NAME, LINK Y CSS

    # -------------------- FUNCIÓN JSON --------------------
    def get_json_file(self, FILE):
        json_path = Inicializar.Json + '/' + FILE + '.json'

        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("Get json_file: " + json_path)
                return self.json_strings
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontró el archivo " + FILE)
            Functions.tearDown(self)

    # -------------------- FUNCIÓN LECTURA DE ENTIDADES --------------------
    def get_entity(self, ENTITY):
        if self.json_strings is False:
            print("Define el DOM para esta prueba")
        else:
            try:
                self.json_ValueToFind = self.json_strings[ENTITY]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[ENTITY]["GetFieldBy"]
                # print("json_ValueToFind: " + f"{self.json_ValueToFind}" + "\n" + "json_GetFieldBy: " + self.json_GetFieldBy)
                return True
            except KeyError:
                pytest.skip(u"get entity: No se encontró la key a la cual se hace referencia: " + ENTITY)
                Functions.tearDown(self)
                return None

    ##########################################################
    ############  <--- BEHAVIOR DRIVEN TEST --->  ############
    ##########################################################
    def get_elements(self, entity):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontró el valor en el JSON definido")

        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "xpath":
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                print("get_elements: " + self.json_ValueToFind)
                return elements

            except NoSuchElementException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown()
