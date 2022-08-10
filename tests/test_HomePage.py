import time
import pytest

from pageObjects.GlobalStudyPage import GlobalStudyPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium import webdriver


class TestHomePage(BaseClass):


    def testHomePageNav(self):

        homepage = HomePage(self.driver)
        homepage.getConfigure().click()


        #time.sleep(1)
        homepage.getConfigureStudySetup().click()
        #time.sleep(1)
        globalStudyPage = GlobalStudyPage(self.driver)
        #time.sleep(1)

        assert globalStudyPage.getStudiesTitle().text == "STUDIES"