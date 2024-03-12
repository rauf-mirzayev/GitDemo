import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.CheckoutPage import CheckoutPage
from pageObject.ConfirmPage import ConfirmationPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        homePage = HomePage(self.driver) #new object

        checkout_page = homePage.shopItems()   #new Object for checkout page created in HomePage.py by clicking in SHOP button
        log.info("Getting all card Titles")
        get_all_Titles = checkout_page.getTitles()
        i = -1
        for product in get_all_Titles:
            i = +1
            phoneText = product.text
            log.info(phoneText)
            if phoneText == "Blackberry":
                checkout_page.getFooterText()[i].click()

        checkout_page.checkout_button().click()

        confPage = checkout_page.checkoutConfirmationButton() #newObject for confirmatiom page created in Checkout.py by clicking in checkoutConfirmationButton

        log.info("Entering country name")
        confPage.country_field().send_keys("er")

        self.verify_Bylink_presence("Germany")

        confPage.country_name().click()

        confPage.purchase_button().click()

        self.verify_bycss_presence(confPage.sucMessage[1])
        message = confPage.alert_suc_message().text
        print(message)

        print("askhfvkahvsjfva") #test git GitDemo project
        print("ssfafdsfs")

        log.info("received text from app is: " + message)
        assert "Success! Thank you! " in message


