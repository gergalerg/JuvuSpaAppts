from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class SplashEmail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
    
    def test_splash_email(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("record_email").clear()
        driver.find_element_by_id("record_email").send_keys("cat@butt.org")
        driver.find_element_by_css_selector("input.landing_sub").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.get(self.base_url + "/admin")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("sforman")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("catbutt")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Emailss").click()
        driver.find_element_by_link_text("<\"cat@butt.org\">").click()
        try:
            self.assertEqual("cat@butt.org", driver.find_element_by_id("id_email").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Delete").click()
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Log out").click()
    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
