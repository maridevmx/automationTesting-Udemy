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
from selenium.webdriver import Edge
from selenium.webdriver.support.ui import Select
import json
import time

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

        elif NAVEGADOR == ('OPERA'):
            self.driver = webdriver.Opera()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        # ---------- CONFIGURACIÓN PENDIENTE
        elif NAVEGADOR == {'EDGE'}:
            self.driver = webdriver.Edge()
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

    ##########################################################################
    #####################  <--- TEXTBOX & COMBO HANDLE --->  #################
    ##########################################################################

    def select_by_text(self, entity, text):
        Functions.get_select_element(self, entity).select_by_visible_text(text)

    def switch_to_parentFrame(self):
        self.driver.switch_to.parent_frame()

    def send_key_text(self, entity, text):
        Functions.get_elements(self, entity).clear()
        Functions.get_elements(self, entity).send_keys(text)

    # -------------------- FUNCIÓN CAMBIO DE 'FRAMES' --------------------
    def switch_to_iframe(self, locator):
        iframe = Functions.get_elements(self, locator)
        self.driver.switch_to.frame((iframe))
        print(f"Se realizó el switch a {locator}")

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
    ##########################  <--- WAIT ELEMENTS --->  #####################
    ##########################################################################
    def esperar(self, timeLoad = 8):
        print("Esperar: Inicia ( " +str(timeLoad) + ")")

        try:
            totalWait = 0
            while (totalWait < timeLoad):
                time.sleep(1)
                totalWait = totalWait + 1
        finally:
            print("Esperar: Carga Finalizada...")
