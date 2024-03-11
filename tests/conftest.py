import os

import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

    parser.addoption(
        "--URL", action="store", default="PROD_ENV"
    )


@pytest.fixture(scope="class")
def setUp(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    URL = request.config.getoption("URL")
    if URL == "QA_ENV":
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    elif URL == "PROD_ENV":
        driver.get("https://misli.az/")

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name, path="C:\\Users\\rauf.mirzoyev\\PycharmProjects\\PythonSellFramework\\report"):
    if not os.path.exists(path):
        os.makedirs(path)
    screenshot_path = os.path.join(path, name)

    driver.get_screenshot_as_file(screenshot_path)
