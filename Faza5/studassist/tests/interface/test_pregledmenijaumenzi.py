import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestPregledmenijaumenzi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    def test_pregledmenijaumenzi(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1722, 2000)
        self.driver.find_element(By.LINK_TEXT, "Menze").click()
        self.driver.find_element(By.CSS_SELECTOR, ".flex-item:nth-child(1) h4").click()
        self.driver.find_element(By.ID, "v-pills-PON").click()
        self.assertEqual(
            self.driver.find_element(By.CSS_SELECTOR, "#v-tab-home-PON > .daily-menu:nth-child(1) > h5").text,
            "Doručak:")
        self.assertEqual(
            self.driver.find_element(By.CSS_SELECTOR, "#v-tab-home-PON > .daily-menu:nth-child(2) > h5").text, "Ručak:")
        self.assertEqual(
            self.driver.find_element(By.CSS_SELECTOR, "#v-tab-home-PON > .daily-menu:nth-child(3) > h5").text,
            "Večera:")
        self.driver.find_element(By.ID, "v-pills-PET").click()
        self.assertEqual(
            self.driver.find_element(By.CSS_SELECTOR, "#v-tab-home-PET > .daily-menu:nth-child(1) > h5").text,
            "Doručak:")
        self.assertEqual(
            self.driver.find_element(By.CSS_SELECTOR, "#v-tab-home-PET > .daily-menu:nth-child(2) > h5").text, "Ručak:")
        self.assertEqual(
            self.driver.find_element(By.CSS_SELECTOR, "#v-tab-home-PET > .daily-menu:nth-child(3) > h5").text,
            "Večera:")

if __name__ == "__main__":
    unittest.main()