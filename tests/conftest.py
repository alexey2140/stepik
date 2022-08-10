import time
import pytest

from pageObjects.LoginPage import LoginPage
from testData import excelDemo
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driverfromfixture = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    # elif browser_name == "firefox":
    #     driverfromfixture = webdriver.Firefox(executable_path="C:\.exe")

    driverfromfixture.get("https://charonqa.medavante.net/UserLogin.aspx?ReturnUrl=%2fDefault.aspx%3fwa%3dwsignin1.0%26wtrealm%3dhttps%253a%252f%252fmaportalqa.medavante.net%26wctx%3drm%253d0%2526id%253dpassive%2526ru%253d%25252f%26wct%3d2020-08-05T07%253a51%253a58Z%26wreply%3dhttps%253a%252f%252fmaportalqa.medavante.net&wa=wsignin1.0&wtrealm=https%3a%2f%2fmaportalqa.medavante.net&wctx=rm%3d0%26id%3dpassive%26ru%3d%252f&wct=2020-08-05T07%3a51%3a58Z&wreply=https%3a%2f%2fmaportalqa.medavante.net")
    driverfromfixture.maximize_window()
    driverfromfixture.implicitly_wait(10)

    loginPage = LoginPage(driverfromfixture)

    loginPage.getUserNameField().send_keys(excelDemo.adminUsername)
    loginPage.getPasswordField().send_keys(excelDemo.adminPassword)
    loginPage.submitForm()



    request.cls.driver = driverfromfixture

    yield
    driverfromfixture.close()

    return driverfromfixture
