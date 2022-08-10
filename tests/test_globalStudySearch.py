import time

import pytest
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

from pageObjects.LoginPage import LoginPage
from pageObjects.GlobalStudyPage import GlobalStudyPage



class TestGlobalStudyPage(BaseClass):

    @pytest.fixture(params=[("Tropicam study")])
    def getData(self, request):
        return request.param


    def test_studySearch(self, getData):
        homepage = HomePage(self.driver)
        homepage.getConfigure().click()
        homepage.getConfigureStudySetup().click()
        globalStudyPage = GlobalStudyPage(self.driver)
        time.sleep(5)
        globalStudyPage.getStudiesTitle().click()
        time.sleep(5)
        globalStudyPage.getsearchField().send_keys("Trop")
        time.sleep(5)
        globalStudyPage.getsearchFieldSubmit()
        time.sleep(5)

        assert globalStudyPage.getGeneralStudyName().text == "NRS Tropicam study"