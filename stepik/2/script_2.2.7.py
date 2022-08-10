from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import math
import time
import os


s = Service("C:\\chromedriver.exe")


browser = webdriver.Chrome(service=s)
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')


browser.find_element(By.NAME, "firstname").send_keys("First Name")
browser.find_element(By.NAME, "lastname").send_keys("Last Name")
browser.find_element(By.NAME, "email").send_keys("Email")

browser.find_element(By.NAME, "file").send_keys(file_path)

browser.find_element(By.XPATH, "// button[text() = 'Submit']").click()

time.sleep(10)
browser.quit()