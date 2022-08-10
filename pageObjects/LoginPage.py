from selenium.webdriver.common.by import By

#from pageObjects import HomePage
from pageObjects.HomePage import HomePage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    userNameField = (By.ID, "WebLogin_UserName")
    passwordField = (By.ID, "Password")
    signInBtn = (By.ID, "WebLogin_Login")

    def getUserNameField(self):
        return self.driver.find_element(*LoginPage.userNameField)

    def getPasswordField(self):
        return self.driver.find_element(*LoginPage.passwordField)

    def getSignInBtn(self):
        return self.driver.find_element(*LoginPage.signInBtn)

    def submitForm(self):
        self.driver.find_element(*LoginPage.signInBtn).click()
        homepage = HomePage(self.driver)
        return homepage
