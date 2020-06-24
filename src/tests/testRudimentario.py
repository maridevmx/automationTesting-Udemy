#################### IMPORTANDO LIBRERÍA DE SELENIUM ####################

from selenium import webdriver
import time

#################### INICIALIZO EL DRIVER ####################
driver = webdriver.Firefox()

#################### HOST DE LA APLICACIÓN ####################
driver.get("http://www.python.org")

#################### SE VERIFICA EL TITULO DE LA APLICACION ####################
assert "Python" in driver.title
time.sleep(20)

#################### ALMACENO EN UNA VARIABLE EL OBJETO QUE VOY A INTERACTUAR ####################
elem = driver.find_element_by_id("id-search-field")

#################### SE LIMPIA EL TXT ####################
elem.clear()

#################### SE ESCRIBE PYCON ####################
elem.send_keys("pycon")

#################### SE CIERRA LA APLICACIÓN ####################
driver.close()