import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setUp")
class BaseClass:

    def verify_Bylink_presence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, text)))

    def verify_bycss_presence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, text)))

    def select_from_dropdown(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("C:\\Users\\rauf.mirzoyev\PycharmProjects\PythonSellFramework\\utilities/logfile.log")  # file kuda tekut logi

        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # format v kotorom mi poluchayem logi
        fileHandler.setFormatter(formatter)  # vizivayem i primenayem

        logger.addHandler(fileHandler)  # obyekt kotoriy dobavvlayet logi v vibranniy file

        logger.setLevel(logging.DEBUG)
        return logger
