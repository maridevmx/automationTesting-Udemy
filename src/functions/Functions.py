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
from src.functions.Inicializar import Inicializar
from selenium import webdriver
from selenium.webdriver.ie.options import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as OptionsChrome

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