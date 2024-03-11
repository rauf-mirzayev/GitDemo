from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    countryName = (By.LINK_TEXT, "Germany")
    purchase = (By.XPATH, "//input[@value='Purchase']")
    sucMessage = (By.CSS_SELECTOR, "div[class*='success']")
    alertMessage = (By.CLASS_NAME, "alert-success")

    def country_field(self):
        return self.driver.find_element(*ConfirmationPage.country)

    def country_name(self):
        return self.driver.find_element(*ConfirmationPage.countryName)

    def purchase_button(self):
        return self.driver.find_element(*ConfirmationPage.purchase)

    def success_message(self):
        return self.driver.find_element(*ConfirmationPage.sucMessage)

    def alert_suc_message(self):
        return self.driver.find_element(*ConfirmationPage.alertMessage)





