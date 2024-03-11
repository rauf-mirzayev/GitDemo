import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("FirstName is: "+getData["firstname"])
        homepage.get_name().send_keys(getData["firstname"])
        log.info("Email is: "+getData["email"])
        homepage.get_email().send_keys(getData["email"])
        homepage.get_password().send_keys(getData["password"])
        homepage.get_checkbox().click()
        homepage.get_student_button().click()
        self.select_from_dropdown(homepage.get_dropdown_list(), getData["gender"])

        homepage.get_submit_Button().click()
        successMessage = homepage.get_success_message().text
        log.info("Received message from app: " + successMessage)
        assert "Success" in successMessage
        self.driver.refresh()

        time.sleep(2)

        #     //tagname[@attribute = 'value'] //input[@type = 'submit'] - (//input[@type='text'])[3] XPATH
        #     tagname[attribute = 'value']    input[name = 'name] - # id, .classname   - CSS selector

    @pytest.fixture(params=HomePageData.get_test_data("TestCase2"))
    def getData(self, request):
        return request.param
