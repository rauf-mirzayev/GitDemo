from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver


    shop = (By.XPATH, "//a[contains(@href,'shop')]")
    name_field = (By.CSS_SELECTOR, "input[name = 'name']")
    email_address = (By.NAME, "email")
    password_field = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    student_button = (By.ID, "inlineRadio1")
    dropdownList = (By.ID, "exampleFormControlSelect1")
    submitButton = (By.XPATH, "//input[@type = 'submit']")
    success_message = (By.CLASS_NAME, "alert-success")



    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name_field)

    def get_email(self):
        return self.driver.find_element(*HomePage.email_address)

    def get_password(self):
        return self.driver.find_element(*HomePage.password_field)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_student_button(self):
        return self.driver.find_element(*HomePage.student_button)
    def get_dropdown_list(self):
        return self.driver.find_element(*HomePage.dropdownList)

    def get_submit_Button(self):
        return self.driver.find_element(*HomePage.submitButton)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.success_message)
