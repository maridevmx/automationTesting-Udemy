import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Test_008(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def test_008(self):

        # -------------------- INGRESO A LA APP --------------------
        self.driver.get("https://www.mercadolibre.com.mx/")
        self.element = "/html[1]/body[1]/main[1]/div[1]/div[1]/section[10]/div[1]/div[1]"

        try:
            wait = WebDriverWait(self.driver,30)
            wait.until(EC.visibility_of_element_located((By.XPATH,self.element)))

        except TimeoutException:
            self.skipTest("No se encuentra el elemento")

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
