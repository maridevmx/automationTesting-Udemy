import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class Test006(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # -------------------- INGRESO A LA APP --------------------
        self.driver.get("http://www.echoecho.com/htmllinks10.htm")

    def test_006(self):

        # -------------------- FRAME PRINCIPAL --------------------
        self.main_Enlace = self.driver.find_element_by_xpath("//span[contains(text(),'Go to Yahoo')]")
        self.main_Enlace.click()
        Ventanas = self.driver.window_handles
        print(Ventanas)
        self.driver.switch_to.window(Ventanas[1])
        time.sleep(5)

        self.driver.switch_to.window(Ventanas[0])
        self.main_Enlace.click()
        self.driver.switch_to.window(Ventanas[0])
        time.sleep(5)




    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
