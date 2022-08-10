from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import math

s = Service("C:\\chromedriver.exe")
browser = webdriver.Chrome(service=s)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока цена не снизится до 100$
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "100"))

button = browser.find_element(By.XPATH, "//button[@id='book']")

button.click()

num1 = browser.find_element(By.ID, "input_value").text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser.find_element(By.ID, "answer").send_keys(calc(num1))

browser.find_element(By.XPATH, "// button[text() = 'Submit']").click()

time.sleep(10)
browser.quit()