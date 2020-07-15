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

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.functions.Inicializar import Inicializar
from selenium import webdriver
from selenium.webdriver.ie.options import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest
import json
import time
import datetime
import re
import os
import openpyxl
import allure
import pyodbc as pyodbc
Scenario = {}
diaGlobal= time.strftime(Inicializar.DateFormat)  # formato aaaa/mm/dd
horaGlobal = time.strftime(Inicializar.HourFormat)  # formato 24 houras



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
            self.driver = webdriver.Firefox(executable_path = Inicializar.baseDir + "\\drivers\\geckodriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        elif NAVEGADOR == ('OPERA'):
            self.driver = webdriver.Opera(executable_path = Inicializar.baseDir + "\\drivers\\operadriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        # ---------- CONFIGURACIÓN PENDIENTE
        elif NAVEGADOR == {'EDGE'}:
            #options = EdgeOptions()
            #options.use_chromium = True
            self.driver = webdriver.Edge(executable_path = Inicializar.baseDir + "\\drivers\\msedgedriver.exe")
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

    ##########################################################################
    #######################  <--- LOCATORS HANDLE --->  ######################
    ##########################################################################

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

    ##########################################################################
    #########################  <--- JSON HANDLE --->  ########################
    ##########################################################################

    # -------------------- FUNCIÓN ABRIR ARCHIVO --------------------
    def get_json_file(self, FILE):
        json_path = Inicializar.Json + '/' + FILE + '.json'

        try:
            with open(json_path, encoding='utf-8') as read_file:
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

    # -------------------- FUNCIÓN PARA OBTENER ELEMENTOS POR IDENTIFICADOR --------------------
    def get_elements(self, entity, MyTextElement = None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            return print("No se encontró el valor en el JSON definido")

        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                print("get_elements: " + self.json_ValueToFind)
                return elements

            except NoSuchElementException:
                print("get_elements: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_elements: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown()

    # -------------------- FUNCIÓN PARA OBTENER ELEMENTOS TIPO 'TEXTO' --------------------
    def get_text(self, entity, MyTextElement = None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            return print("No se encontró el valor en el JSON definido")

        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                print("get_ text: " + self.json_ValueToFind )
                print("Text Value: " + elements.text)
                return elements.text

            except NoSuchElementException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown()

    ##########################################################################
    #########################  <--- WAIT ELEMENTS --->  ######################
    ##########################################################################

    # -------------------- FUNCIÓN LECTURA DE 'WAITS' --------------------
    def esperar_elemento(self, locator, MyTextElement = None):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontró el valor en el JSON definido")

        else:
            try:
                if self.json_GetFieldBy.lower == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u"Esperar elemento: Se desplegó el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME,self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"Esperar elemento: Se desplegó el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)

                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(u"Esperar elemento: Se desplegó el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(u"Esperar elemento: Se desplegó el elemento " + locator)
                    return True

            except TimeoutException:
                print("esperar_elemento: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

            except NoSuchElementException:
                print("esperar_elemento: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

    # -------------------- FUNCIÓN LECTURA DE 'SELECT' --------------------
    def get_select_element(self, entity):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            return print("No se encontró el valor en el JSON definido")

        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    select = Select(self.driver.find_element_by_id(self.json_ValueToFind))

                elif self.json_GetFieldBy.lower() == "name":
                    select = Select(self.driver.find_element_by_name(self.json_ValueToFind))

                elif self.json_GetFieldBy.lower() == "xpath":
                    select = Select(self.driver.find_element_by_xpath(self.json_ValueToFind))

                elif self.json_GetFieldBy.lower() == "link":
                    select = Select(self.driver.find_element_by_partial_link_text(self.json_ValueToFind))

                print("get_select_element: " + self.json_ValueToFind)
                return select

                # USO

                # select by visible text # select.select_by_visible_text('Texto')

                # select by value # select.select_by_value('1')

            except TimeoutException:
                print("get_select_element: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

            except NoSuchElementException:
                print("get_select_element: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

    def alert_windows(self, accept = "accept"):

        try:
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.alert_is_present(), print("Esperando alerta..."))

            alert = self.driver.switch_to.alert

            print(alert.text)

            if accept.lower() == "accept":
                alert.accept()
                print("Click in Accept")
            else:
                alert.dismiss()
                print("Click in Dismiss")
        except NoAlertPresentException:
            print("Alerta no presente")
        except NoSuchWindowException:
            print("Alerta no presente")
        except TimeoutException:
            print("Alerta no presente")

    def esperar(self, timeLoad = 8):
        print("Esperar: Inicia ( " +str(timeLoad) + ")")

        try:
            totalWait = 0
            while (totalWait < timeLoad):
                time.sleep(1)
                totalWait = totalWait + 1
        finally:
            print("Esperar: Carga Finalizada...")

    ##########################################################################
    #####################  <--- TEXTBOX & COMBO HANDLE --->  #################
    ##########################################################################

    # -------------------- FUNCIÓN QUE OBTIENE EL TEXTO DE UN 'DROP-DOWN' --------------------
    def select_by_text(self, entity, text):
        Functions.get_select_element(self, entity).select_by_visible_text(text)

    # -------------------- FUNCIÓN ESCRIBE TEXTO EN UN ELEMENTO --------------------
    def send_key_text(self, entity, text):
        Functions.get_elements(self, entity).clear()
        # Functions.send_especific_keys(self, entity, "Del")
        Functions.get_elements(self, entity).send_keys(text)

    # -------------------- FUNCIÓN QUE ENVIA KEYS ESPECIALES --------------------
    def send_especific_keys(self, element, key):
        if key == 'Enter':
            Functions.get_elements(self, element).send_keys(Keys.ENTER)

        elif key == 'Tab':
            Functions.get_elements(self, element).send_keys(Keys.TAB)

        elif key == 'Space':
            Functions.get_elements(self, element).send_keys(Keys.SPACE)

        elif key == 'Del':
            Functions.get_elements(self, element).send_keys(Keys.chord(Keys.CONTROL,"a", Keys.DELETE))

        elif key == 'Back':

            lenText = Functions.get_elements(self, element).text

            while lenText == 0:
                Functions.get_elements(self, element).send_keys(Keys.BACK_SPACE)
                lenText = lenText -1

        time.sleep(3)

    # -------------------- FUNCIÓN CAMBIO DE 'FRAMES' --------------------
    def switch_to_iframe(self, locator):
        iframe = Functions.get_elements(self, locator)
        self.driver.switch_to.frame((iframe))
        print(f"Se realizó el switch a {locator}")

    # -------------------- FUNCIÓN QUE OBTIENE EL FRAME 'PADRE' --------------------
    def switch_to_parentFrame(self):
        self.driver.switch_to.parent_frame()

    # -------------------- FUNCIÓN CAMBIO DE VENTANA POR NOMBRE --------------------
    def switch_to_windows_name(self, ventana):
        if ventana in self.ventanas:
            self.driver.switch_to.window(self.ventanas[ventana])
            Functions.page_has_loaded(self)
            print("Volviendo a " + ventana + " : " + self.ventanas[ventana])
        else:
            self.nWindows = len(self.driver.window_handles) -1
            self.ventanas[ventana] = self.driver.window_handles[int(self.nWindows)]
            self.driver.switch_to.window(self.ventanas[ventana])
            self.driver.maximize_window()
            print(self.ventanas)
            print("Estas en " + ventana + " : " + self.ventanas[ventana])
            Functions.page_has_loaded(self)

    ##########################################################################
    ###########################  <--- JAVASCRIPT --->  #######################
    ##########################################################################

    # -------------------- FUNCIÓN 'ABRIR NUEVA PESTAÑA' --------------------
    def new_window(self, URL):
        self.driver.execute_script(f'''window.open("{URL}","_blank");''')
        Functions.page_has_loaded(self)

    # -------------------- FUNCIÓN PARA VERIFICAR EL CARGADO COMPLETO DE LA PÁGINA --------------------
    def page_has_loaded(self):
        driver = self.driver
        print("Checking if {} page is loaded. ".format(self.driver.current_url))
        page_state = driver.execute_script('return document.readyState')
        yield
        WebDriverWait(driver, 30).until(lambda driver: page_state == 'complete')
        assert page_state == 'complete', "No se completó la carga"

    # -------------------- FUNCIÓN PARA REALIZAR SCROLL A LA PÁGINA --------------------
    def scroll_to(self, locator):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontró el valor en el Json definido")

        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
                    print(u"scroll_to by ID: " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "xpath":
                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
                    print(u"scroll_to by XPATH: " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
                    print(u"scroll_to by LINK: " + locator)
                    return True

            except TimeoutException:
                print(u"scroll_to: El " + locator + " no está presente")
                Functions.tearDown(self)

    # -------------------- FUNCIÓN PARA CLIC SOBRE UN ELEMENTO --------------------
    def js_clic(self, locator, MyTextElement = None):
        Get_Entity = Functions.get_entity(self, locator)
        Functions.esperar_elemento(self, locator, MyTextElement)

        if Get_Entity is None:
            return print("No se encontró el valor en el Json definido")

        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"js_clic by ID: " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)

                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"js_clic by XPATH: " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"js_clic by LINK: " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "name":
                    localizador = self.driver.find_element(By.NAME, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"js_clic by NAME: " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "css":
                    localizador = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"js_clic by CSS: " + locator)
                    return True

            except TimeoutException:
                print(u"js_clic: El " + locator + " no está presente")
                Functions.tearDown(self)

    ##########################################################################
    ##########################  <--- VERIFICACIÓN --->  ######################
    ##########################################################################
    def assert_text(self, locator, texto):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontró el valo en el Json definido")

        else:
            if self.json_GetFieldBy.lower() == "id":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_all_elements_located((By.ID, self.json_ValueToFind)))
                objText = self.driver.find_element_by_id(self.json_ValueToFind).text

            elif self.json_GetFieldBy.lower() == "name":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_all_elements_located((By.NAME, self.json_ValueToFind)))
                objText = self.driver.find_element_by_name(self.json_ValueToFind).text

            elif self.json_GetFieldBy.lower() == "xpath":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_all_elements_located((By.XPATH, self.json_ValueToFind)))
                objText = self.driver.find_element_by_xpath(self.json_ValueToFind).text

            elif self.json_GetFieldBy.lower() == "link":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                objText = self.driver.find_element_by_partial_link_text(self.json_ValueToFind).text

            elif self.json_GetFieldBy.lower() == "css":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                objText = self.driver.find_element_by_css_selector(self.json_ValueToFind).text

        print("Verificar texto -> el valor mostrado en: " + locator + " es: " + objText + " el esperado es: " + texto)
        assert texto == objText, "Los valores comparados no coinciden"

    # -------------------- FUNCIÓN BOOLEANA PARA VERIFICAR LA EXISTENCIA DE UN ELEMENTO --------------------
    def check_element(self, locator):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontró el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    print(u"check_element: Se visualizó el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    print(u"check_element: Se visualizó el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    print(u"check_element: Se visualizó el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, self.json_ValueToFind)))
                    print(u"check_element: Se visualizó el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print(u"check_element: Se visualizó el elemento " + locator)
                    return True

            except NoSuchElementException:
                print("check_element: No se encontró el elemento: " + self.json_ValueToFind)
                return False

            except TimeoutException:
                print("check_element: No se encontró el elemento: " + self.json_ValueToFind)
                return False

    def validar_elemento(self, locator):
        Get_Entity = Functions.get_entity(self, locator)

        TIME_OUT = 10

        if Get_Entity is None:
            return print("No se encontró el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, TIME_OUT)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u"validar_elemento clickable: Se visualizó el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, TIME_OUT)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"validar_elemento clickable: Se visualizó el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, TIME_OUT)
                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(u"validar_elemento clickable: Se visualizó el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, TIME_OUT)
                    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.json_ValueToFind)))
                    print(u"validar_elemento clickable: Se visualizó el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, TIME_OUT)
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print(u"validar_elemento clickable: Se visualizó el elemento " + locator)
                    return True

            except TimeoutException:
                print("validar_elemento clickable: No se encontró el elemento: " + self.json_ValueToFind)
                return False
    ##########################################################################
    ########################  <--- DATA DE ESCENARIO --->  ###################
    ##########################################################################

    def create_variable_scenary(self, key, value):
        Scenario[key] = value
        print(Scenario)
        print("Se almacenó la key " + key + " : " + value)

    def save_variable_scenary(self, element, variable):
        Scenario[variable] = Functions.get_text(self, element)
        print(Scenario)
        print("Se almacenó el valor " + variable + " : " + Scenario[variable])

    def get_variable_scenary(self, variable):
        self.variable = Scenario[variable]
        print(f"get_variable_scenary: {self.variable}")
        return self.variable

    def compare_with_variable_scenary(self, element, variable):
        variable_scenary = str(Scenario[variable])
        element_text = str(Functions.get_text(self, element))
        exist = (variable_scenary in element_text)
        print(exist)
        print(f"Comparando los valores ... Verificando si {variable_scenary} está presente en {element_text} : {exist}")
        assert  exist == True, f"{variable_scenary} != {element_text}"

    def textDataEnvironmentReplace(self, text):
        if text == 'today':
            self.today = datetime.date.today()
            text = self.today.strftime(Inicializar.DateFormat)

        elif text == 'yesterday':
            self.today = datetime.date.today() - datetime.timedelta(days = 1)
            text = self.today.strftime(Inicializar.DateFormat)

        elif text == 'last month':
            self.today = datetime.date.today() - datetime.timedelta(days = 30)
            text = self.today.strftime(Inicializar.DateFormat)

        return text

    # -------------------- FUNCIÓN PARA MANEJO DE ARCHIVOS EXCEL --------------------
    def leer_celda(self, celda):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        sheet = wb["DataTest"]
        valor = str(sheet[celda].value)
        print(u"------------------------------------")
        print(u"El libro de excel utilizado es: " + Inicializar.Excel)
        print(u"El valor de la celda es: " + valor)
        print(u"------------------------------------")
        return valor

    def escribir_celda(self, celda, valor):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        hoja = wb["DataTest"]
        hoja[celda] = valor
        wb.save(Inicializar.Excel)
        print(u"------------------------------------")
        print(u"El libro de excel utilizado es: " + Inicializar.Excel)
        print(u"Se escribio en la celda: " + str(celda) + u" el valor: " + str(valor))
        print(u"------------------------------------")

    ##########################################################################
    ##########################  <--- BASE DE DATOS --->  #####################
    ##########################################################################

    def pyodbc_conn(self, host = Inicializar.DB_HOST, port = Inicializar.DB_PORT, dbname = Inicializar.DB_DATABASE, user = Inicializar.DB_USER, password = Inicializar.DB_PASS):
        try:
            configDB = dict(server = host,
                            port = port,
                            database = dbname,
                            username = user,
                            password = password)

            connection = ('SERVER={server};' 
                         'PORT={port};' +
                         'DATABASE={database};' +
                         'UID={username};' +
                         'PWD={password}')

            conn = pyodbc.connect(r'Driver={Oracle in XE};dbq=XE;' +
                                  connection.format(**configDB))

            self.cursor = conn.cursor()
            print("Always connected")
            return self.cursor

        except (pyodbc.OperationalError) as error:
            self.cursor = None
            pytest.skip("Error en conexión a la base de datos: " + str(error))

    def pyodbc_query(self, query):
        self.cursor = Functions.pyodbc_conn(self)

        if self.cursor is not None:
            try:
                print("pyodbc_query: " + query)
                self.cursor.execute(query)
                self.result = self.cursor.fetchall()
                for row in self.result:
                    print(row)

            except (pyodbc.Error) as error:
                print("Error en la consulta: ", error)
            finally:
                if (self.cursor):
                    self.cursor.close()
                    print("pyodbc_query: Se cerró la conexión")

    ##########################################################################
    #######################  <--- CAPTURA DE PANTALLA --->  ##################
    ##########################################################################

    def hora_actual(self):
        self.hora = time.strftime(Inicializar.HourFormat) # Formato de 24 hrs.
        return self.hora

    def crear_path(self):
        dia = time.strftime("%d-%m-%Y") # formato aaaa/mm/dd
        generalPath = Inicializar.Path_Evidencias
        driverTest = Inicializar.Navegador
        testCase = self.__class__.__name__
        horaActual = horaGlobal
        getContext = re.search("Contexto: " , testCase)

        if getContext:
            path = f"{generalPath}/{dia}/{driverTest}/{horaActual}/"
        else:
            path = f"{generalPath}/{dia}/{testCase}/{driverTest}/{horaActual}/"
        if not os.path.exists(path): # Si no existe el directorio, lo crea
            os.makedirs(path)
        return path

    def capturar_pantalla(self):
        path = self.crear_path()
        testCase = self.__class__.__name__
        img = f'{path}/{testCase}_(' + str(self.hora_actual()) + ')' + '.png'
        self.driver.get_screenshot_as_file(img)
        print(img)
        return img

    def captura(self, descripcion):
        allure.attach(self.driver.get_screenshot_as_png(), descripcion, attachment_type = allure.attachment_type.PNG)



