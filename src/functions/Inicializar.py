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

    # JsonData
    Json = baseDir + u'/pages'

    # Environment
    Environment = 'Dev'

    # BROWSER DE PRUEBAS
    Navegador = u'FIREFOX'

    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = baseDir + u'/data/capturas'

    # HOJA DE DATOS EXCEL
    Excel = baseDir + u'/data/Data.xlsx'

    # CONFIGURACIÓN DE ENTORNOS
    if Environment == 'Dev':
        URL = 'https://www.spotify.com/mx/signup/'
        User = 'UdemyTest'
        Pass = 'UdemyTestPython'

    if Environment == 'Test':
        URL = 'https://www.despegar.com.mx/'
        User = 'UdemyTest'
        Pass = 'UdemyTestPython'