from selenium.webdriver.common.by import By

class GlobalStudyPage:

    searchField = (By.XPATH, "//div[@class='input-group']/*[1]")
    searchFieldSubmit = (By.XPATH, "//input[@name='search']/following-sibling::span")
    firstStudyItemInSearch = (By.XPATH, "//div[@class='scroll-wrapper']//span[contains(text(),'Tropicam')]")
    generalStudyName = (By.XPATH, "//div[@class='admin-grid-row ng-scope even']/*[1]")
    studiesTitle = (By.XPATH, "//span[.='Studies']")

    def __init__(self, driver):
        self.driver = driver





    def getSearchItem(self):
        return self.driver.find_element(*GlobalStudyPage.firstStudyItemInSearch)

    def getGeneralStudyName(self):
        return self.driver.find_element(*GlobalStudyPage.generalStudyName)

    def getsearchField(self):
        return self.driver.find_element(*GlobalStudyPage.searchField)

    def getsearchFieldSubmit(self):
        return self.driver.find_element(*GlobalStudyPage.searchFieldSubmit)

    def getStudiesTitle(self):
        return self.driver.find_element(*GlobalStudyPage.studiesTitle)
