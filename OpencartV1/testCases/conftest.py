import datetime
import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime
@pytest.fixture()
def setup(browser):
    if browser=='edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser=='firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

##### pytest html report #######

def pytest_configure(config):
    config._metadata['Project Name']= 'OpenartV1'
    config._metadata['Module Name']= 'Custregration'
    config._metadata['Tester'] = 'Manoj'


@pytest.mark.optionalhook
def pytest_Metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath =os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"


















