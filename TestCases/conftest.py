from selenium import webdriver
import pytest
import undetected_chromedriver as uc



@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = uc.Firefox()
    else:
        driver = uc.Ie()
    return driver

# this will get the value from CLI/hooks
def pytest_addoption(parser):
    parser.addoption('--browser')

#     this will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")