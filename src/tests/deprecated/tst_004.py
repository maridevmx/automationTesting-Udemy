import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test004(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NOMBRE = "Mariela"
        self.APELLIDO = "Mdza"
        self.USUARIO = "cursopruebas2020"
        self.PASSWORD = "Cursopruebas2020-A"

    def test_004(self):
        NOMBRE = "Mariela"

        # INGRESO A LA APP DE REGISTRO
        self.driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        # COLOCAR NOMBRE
        #self.driver.find_element_by_id("firstName").clear()
        #self.driver.find_element_by_id("firstName").send_keys(self.NOMBRE)
        self.driver.find_element_by_name("firstName").clear()
        self.driver.find_element(By.NAME,"firstName").send_keys(self.NOMBRE)
        time.sleep(2)

        # COLOCAR APELLIDO
        #self.driver.find_element_by_xpath("//*[@id='lastName']").clear()
        #self.driver.find_element_by_xpath("//*[@id='lastName']").send_keys(self.APELLIDO)
        self.driver.find_element_by_css_selector("#lastName").clear()
        self.driver.find_element(By.NAME, "lastName").send_keys(self.APELLIDO)
        time.sleep(2)

        # PARTIAL LINK TEST
        self.driver.find_element_by_partial_link_text("Ayuda").click()

        # lastName
        # COLOCAR USERNAME
        #self.driver.find_element_by_name("Username").clear()
        #self.driver.find_element_by_name("Username").send_keys(self.USUARIO)
        #time.sleep(2)

        # COLOCAR PASSWORD
        #self.driver.find_element_by_xpath("//*[@id='passwd']/div[1]/div/div[1]/input").clear()
        #self.driver.find_element_by_xpath("//*[@id='passwd']/div[1]/div/div[1]/input").send_keys(self.PASSWORD)
        #time.sleep(2)

        # CONFIRMACIÓN DE PASSWORD
        #self.driver.find_element_by_xpath("//*[@id='confirm-passwd']/div[1]/div/div[1]/input").clear()
        #self.driver.find_element_by_xpath("//*[@id='confirm-passwd']/div[1]/div/div[1]/input").send_keys(self.PASSWORD)
        #time.sleep(2)

        # BOTÓN NEXT
        # self.driver.find_element_by_xpath("//*[@id='accountDetailsNext']/span/span").click()
        # time.sleep(2)

        # MENSAJE DE ERROR
        # MENSAJE_ERROR = self.driver.find_element_by_xpath("//*[@id='view_container']/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div")

        # assert MENSAJE_ERROR == "Elige una dirección de Gmail"
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
