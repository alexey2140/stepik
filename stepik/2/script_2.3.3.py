from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import math
import time
import os


s = Service("C:\\chromedriver.exe")


browser = webdriver.Chrome(service=s)
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)


browser.find_element(By.XPATH, "//button").click()

confirm = browser.switch_to.alert
confirm.accept()


num1 = browser.find_element(By.ID, "input_value").text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser.find_element(By.ID, "answer").send_keys(calc(num1))

browser.find_element(By.XPATH, "// button[text() = 'Submit']").click()

time.sleep(10)
browser.quit()
