from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmationPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # phone = product.find_element(By.XPATH, "div/h4/a").text
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    addButton = (By.XPATH, "a[class*='btn-primary']")
    checkoutButton = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    checkout_confirmation_button = (By.XPATH, "//button[@class='btn btn-success']")

    def getTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getFooterText(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def addToCard(self):
        return self.driver.find_element(*CheckoutPage.addButton)

    def checkout_button(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def checkoutConfirmationButton(self):
        self.driver.find_element(*CheckoutPage.checkout_confirmation_button).click()
        confPage = ConfirmationPage(self.driver)
        return confPage


