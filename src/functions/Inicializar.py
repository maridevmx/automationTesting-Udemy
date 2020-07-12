#############################
# Curso:    Selenium Testing Framework con Python ¡De novato a experto! - Udemy
# Tema:     Inicializar configuraciones
# Autor:    M.M.
# Fecha:    25/06/2020
#
# Descripción: Se realizan las primeras configuraciones
#
###############################
# Log:
# 25/06/2020    MMM - Se crea el archivo
################################

import os

class Inicializar():

    # Directorio Base
    baseDir = os.path.abspath(os.path.join(__file__,"../.."))
    DateFormat = "%d/%m/%Y"
    HourFormat = "%H%M%S"

    # JsonData
    Json = baseDir + u'/pages'

    # Environment
    Environment = 'Dev'

    # BROWSER DE PRUEBAS
    Navegador = u'FIREFOX'

    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = baseDir + u'/data/capturas'

    # HOJA DE DATOS EXCEL
    Excel = baseDir + u'/data/DataTest.xlsx'

    # CONFIGURACIÓN DE ENTORNOS
    if Environment == 'Dev':
        URL = 'https://www.spotify.com/mx/signup/'
        User = 'UdemyTest'
        Pass = 'UdemyTestPython'
        DB_HOST = 'localhost'
        DB_PORT = '1521'
        DB_DATABASE = 'BD_SDFT_INS_WEB'
        DB_USER = 'APP_SDFT_INS_WEB'
        DB_PASS = 'APP_SDFT_INS_WEB'

    if Environment == 'Test':
        URL = 'https://www.despegar.com.mx/'
        User = 'UdemyTest'
        Pass = 'UdemyTestPython'