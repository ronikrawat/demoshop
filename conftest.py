from selenium import webdriver
from POM.homepage import Homepage
from POM.login import LoginPage
from POM.registration import Registration
from pytest import fixture
from utilites.lib import SeleniumWrapper


def pytest_addoption(parser):
    # parser.addoption("--env",action= "store",default="test",dest="env")
    parser.addoption("--browser", action="store", default="chrome", dest="browser")


@fixture
def driver(request):
    browser = request.config.option.browser
    if browser.upper() == "CHROME":
        _driver = webdriver.Chrome()
    elif browser.upper() == "EDGE":
        _driver = webdriver.Edge()
    elif browser.upper() == "FIREFOX":
        _driver = webdriver.Firefox()
    else:
        raise Exception("Invalid browser")
    _driver.get("https://demowebshop.tricentis.com/")
    _driver.maximize_window()
    yield _driver
    _driver.quit()


@fixture
def pages(driver):
    class Pages:
        homepage = Homepage(driver)
        loginpage = LoginPage(driver)
        registration = Registration(driver)

    return Pages()
