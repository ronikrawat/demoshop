from utilites.lib import SeleniumWrapper
from utilites.excel_lib import set_locator


@set_locator("homepage")
class Homepage:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def click_login(self):
        self.wrapper.click_element(self.lnk_login)

    def click_registration(self):
        self.wrapper.click_element(self.lnk_register)
