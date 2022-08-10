from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time
from tests import conftest

class FormDesignerPage:

    linkBlockInToolBox = (By.XPATH, "//span[contains(@class, 'block-toolbox-item-text ng-binding') and text() = 'Link']")
    emptyCanvasArea = (By.XPATH, "//div[@class='block-designer-empty-msg ng-binding ng-scope']")
    addLinkValidationMessage = (By.XPATH, "//i[@class='indented-text ng-binding' and text()='link number value should be not less than 1']")

    #emptyCanvasArea1 =
    #addLinkValidationMessage1 =


    def __init__(self, driver):
        self.driver = driver


    def add_link_block_on_canvas(self):
        driver = self.driver
        source = FormDesignerPage.linkBlockInToolBox
        target = FormDesignerPage.emptyCanvasArea
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(source, 250, 250).perform()
