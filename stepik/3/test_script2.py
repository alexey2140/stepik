from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pytest
import unittest


class TestAbs(unittest.TestCase):


    def test_abs1(self):
        s = Service("/usr/local/bin/chromedriver")
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(service=s)
        browser.get(link)
        first_name = browser.find_element(By.XPATH, "//label[contains(text(), 'First name*')]/following-sibling::input")
        last_name = browser.find_element(By.XPATH, "//label[contains(text(), 'Last name*')]/following-sibling::input")
        email = browser.find_element(By.XPATH, "//label[contains(text(), 'Email*')]/following-sibling::input")
        first_name.send_keys("First Name")
        last_name.send_keys("Last Name")
        email.send_keys("email")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(5)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    def test_abs2(self):
        s = Service("/usr/local/bin/chromedriver")
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(service=s)
        browser.get(link)
        first_name = browser.find_element(By.XPATH, "//label[contains(text(), 'First name*')]/following-sibling::input")
        last_name = browser.find_element(By.XPATH, "//label[contains(text(), 'Last name*')]/following-sibling::input")
        email = browser.find_element(By.XPATH, "//label[contains(text(), 'Email*')]/following-sibling::input")
        first_name.send_keys("First Name")
        last_name.send_keys("Last Name")
        email.send_keys("email")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(5)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)



if __name__ == "__main__":
    unittest.main()