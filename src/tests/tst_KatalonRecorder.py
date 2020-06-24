# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.spotify.com/mx/signup/")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("test18Spotify@gmail.com")
        driver.find_element_by_id("confirm").click()
        driver.find_element_by_id("confirm").clear()
        driver.find_element_by_id("confirm").send_keys("test18Spotify@gmail.com")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("PruebaContra")
        driver.find_element_by_id("displayname").click()
        driver.find_element_by_id("displayname").clear()
        driver.find_element_by_id("displayname").send_keys("Test18Spotity")
        driver.find_element_by_id("day").click()
        driver.find_element_by_id("day").clear()
        driver.find_element_by_id("day").send_keys("18")
        driver.find_element_by_id("month").click()
        Select(driver.find_element_by_id("month")).select_by_visible_text("Septiembre")
        driver.find_element_by_id("month").click()
        driver.find_element_by_id("year").click()
        driver.find_element_by_id("year").clear()
        driver.find_element_by_id("year").send_keys("1989")
        driver.find_element_by_xpath("//div[@id='__next']/main/div[2]/form/div[6]/div[2]/label[2]/span").click()
        driver.find_element_by_xpath("//div[@id='__next']/main/div[2]/form/div[7]/label/span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=4 | ]]
        driver.find_element_by_xpath("//span[@id='recaptcha-anchor']/div").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
