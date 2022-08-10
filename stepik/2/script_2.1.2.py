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

    people_radio = browser.find_element(By.ID, "peopleRule")

    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

finally:
    time.sleep(10)
    browser.quit()