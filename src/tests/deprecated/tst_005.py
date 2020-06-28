import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class Test005(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # -------------------- INGRESO A LA APP --------------------
        self.driver.get("https://chercher.tech/practice/frames-example-selenium-webdriver")

    def test_005(self):

        # -------------------- FRAME PRINCIPAL --------------------
        self.main_Titulo = self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]")
        print(self.main_Titulo.text)
        time.sleep(5)

        # -------------------- IR A FRAME 2 --------------------
        self.frame2 = self.driver.find_element_by_xpath("//iframe[@id='frame2']")
        self.driver.switch_to.frame(self.frame2)
        self.frame2_Select = Select(self.driver.find_element_by_xpath("//select[@id='animals']"))
        self.frame2_Select.select_by_visible_text("Baby Cat")
        time.sleep(5)

        # -------------------- VOLVER AL FRAME PRINCIPAL --------------------
        self.driver.switch_to.parent_frame()

        # -------------------- IR A FRAME 1 --------------------
        self.frame1 = self.driver.find_element_by_xpath("//iframe[@id='frame1']")
        self.driver.switch_to.frame(self.frame1)
        self.frame1_text = self.driver.find_element_by_xpath("/html[1]/body[1]/input[1]")
        self.frame1_text.send_keys("Hola Chicos Udemy")
        time.sleep(5)

        # -------------------- IR A FRAME 3 --------------------
        self.frame3 = self.driver.find_element_by_xpath("//iframe[@id='frame3']")
        self.driver.switch_to.frame(self.frame3)
        self.frame3_CheckBox = self.driver.find_element_by_xpath("//input[@id='a']")
        self.frame3_CheckBox.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
