from selenium.webdriver.common.by import By
import time
from pageObjects.GlobalStudyPage import GlobalStudyPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver # driver of the HomePage object takes driver which came in parameters

    title = (By.XPATH, "//div[@id='page-title']/h1")
    navConfigure = (By.XPATH, "//span[contains(text(),'CONFIGURE')]")
    configureStudySetup = (By.XPATH, "//a[contains(text(),'Study Setup')]")

    def getTitle(self):
        return self.driver.find_element(*HomePage.title)

    def getConfigure(self):
        return self.driver.find_element(*HomePage.navConfigure)

    def getConfigureStudySetup(self):
        return self.driver.find_element(*HomePage.configureStudySetup)