import time
import pytest
from testData import excelDemo
from pageObjects.FormDesignerPage import FormDesignerPage
from utilities.BaseClass import BaseClass
from selenium import webdriver


class TestFormDesignerPage(BaseClass):


    def test_adding_link_block_on_canvas(self):

        self.driver.get(excelDemo.formTemplateLink)
        FormDesignerPage.add_link_block_on_canvas(self)

        time.sleep(10)

        assert FormDesignerPage.addLinkValidationMessage.text() == "link number value should be not less than 1"