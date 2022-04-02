from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        s = Service("C://Users//selfg//chromedriver//chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    # elif browser == "firefox":
    #     driver = webdriver.Firefox()
    else:
        s = Service("C://Users//selfg//chromedriver//chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # this will return browser value to setup method
    return request.config.getoption("--browser")


############################# html report ############################

def pytest_configure(config):
    config._metadata['Project Name']= 'Nop Commerce'
    config._metadata['Module Name']= 'Customer'
    config._metadata['tester']='Mayur Baviskar'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)