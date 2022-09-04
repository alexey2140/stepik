import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


@pytest.mark.parametrize('lesson_id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905", "236898"])
def test_with_params(browser, lesson_id):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{lesson_id}/step/1"
    browser.get(link)
    time.sleep(3)
    browser.find_element(By.XPATH, "//div[@class='quiz-component ember-view']/textarea").send_keys(answer)
    #time.sleep(2)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    #time.sleep(2)
    browser.find_element(By.XPATH, "//p[@class='smart-hints__hint']")
    actual_result = browser.find_element(By.XPATH, "//p[@class='smart-hints__hint']").text
    expected_result = "Correct!"
    assert actual_result == expected_result, \
        f"expected {expected_result}, got {actual_result}"
    browser.quit()
