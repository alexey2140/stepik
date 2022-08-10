from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import math
import time


s = Service("C:\\chromedriver.exe")


browser = webdriver.Chrome(service=s)
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

num1 = browser.find_element(By.ID, "input_value").text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


button = browser.find_element(By.XPATH, "// button[text() = 'Submit']")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

browser.find_element(By.ID, "answer").send_keys(calc(num1))
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

browser.find_element(By.ID, "robotCheckbox").click()
browser.find_element(By.ID, "robotsRule").click()

browser.find_element(By.XPATH, "// button[text() = 'Submit']").click()

time.sleep(10)
browser.quit()