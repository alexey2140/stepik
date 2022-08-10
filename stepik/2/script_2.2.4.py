from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:\\chromedriver.exe")


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(service=s)
    browser.get(link)
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    time.sleep(10)
    browser.quit()