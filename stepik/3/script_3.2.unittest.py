from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest

#s = Service("C:\\chromedriver.exe")
s = Service("/usr/local/bin/chromedriver")


link = "http://suninjuly.github.io/registration1.html"
#link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome(service=s)
browser.get(link)

# Ваш код, который заполняет обязательные поля
first_name = browser.find_element(By.XPATH, "//label[contains(text(), 'First name*')]/following-sibling::input")
last_name = browser.find_element(By.XPATH, "//label[contains(text(), 'Last name*')]/following-sibling::input")
email = browser.find_element(By.XPATH, "//label[contains(text(), 'Email*')]/following-sibling::input")

first_name.send_keys("First Name")
last_name.send_keys("Last Name")
email.send_keys("email")

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(10)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()