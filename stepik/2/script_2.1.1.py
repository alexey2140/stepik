from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math

s = Service("C:\\chromedriver.exe")


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome(service=s)
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element(By.ID, "input_value").text

    input = browser.find_element(By.ID, "answer")
    input.send_keys(calc(x))

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    submit = browser.find_element(By.XPATH, "//button[text()= 'Submit']")
    submit.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()