from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math

s = Service("C:\\chromedriver.exe")


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome(service=s)
    browser.get(link)

    treasure = browser.find_element(By.ID, "treasure")
    valuex = treasure.get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser.find_element(By.ID, "answer").send_keys(calc(valuex))
    browser.find_element(By.ID, "robotCheckbox").click()

    browser.find_element(By.ID, "robotsRule").click()

    browser.find_element(By.XPATH, "// button[text() = 'Submit']").click()



finally:
    time.sleep(10)
    browser.quit()