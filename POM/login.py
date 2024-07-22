from utilites.lib import SeleniumWrapper
from utilites.excel_lib import set_locator


@set_locator("loginpage")
class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def login(self, email, password):
        self.wrapper.send_text(self.txt_email, email)
        self.wrapper.send_text(self.txt_password, password)
        self.wrapper.click_element(self.btn_login)

    def login_status(self, email):
        return self.wrapper.element_is_displayed(("xpath", f'//a[text()="{email}"]'))
