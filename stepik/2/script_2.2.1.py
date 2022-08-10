from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:\\chromedriver.exe")


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(service=s)
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text


    result = int(num1) + int(num2)
    locator = "//option[contains(@value, '{fvalue}')]".format(fvalue=result)

    browser.find_element(By.ID, "dropdown").click()
    browser.find_element(By.XPATH, locator).click()

    browser.find_element(By.XPATH, "// button[text() = 'Submit']").click()



finally:
    time.sleep(10)
    browser.quit()