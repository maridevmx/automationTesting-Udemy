import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_007(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NOMBRE = "Mariela"
        self.APELLIDO = "Mdza"
        self.USUARIO = "cursopruebas2020"
        self.PASSWORD = "Cursopruebas2020-A"

    def test_007(self):

        # -------------------- INGRESO A LA APP --------------------

        self.driver.get("https://www.mercadolibre.com.mx/")
        self.element = "/html[1]/body[1]/main[1]/div[1]/div[1]/section[10]/div[1]/div[1]"
        wait = WebDriverWait(self.driver,30)
        wait.until(EC.visibility_of_element_located((By.XPATH,self.element)))

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
