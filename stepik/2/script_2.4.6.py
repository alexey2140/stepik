from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:\\chromedriver.exe")
browser = webdriver.Chrome(service=s)
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

link = "http://suninjuly.github.io/wait1.html"

browser.get(link)

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

time.sleep(10)
browser.quit()