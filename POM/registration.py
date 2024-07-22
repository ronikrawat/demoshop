from utilites.lib import SeleniumWrapper
from utilites.excel_lib import set_locator


@set_locator("registrationpage")
class Registration:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def register_user(self, pages, gender, fname, lname, email, password,
                      confirmpassword):
        if gender.upper() == "MALE":
            self.wrapper.click_element(self.rdo_male)
        elif gender.upper() == "FEMALE":
            self.wrapper.click_element(self.rdo_female)
        else:
            raise Exception("Invalid Gender")
        self.wrapper.send_text(self.txt_fname, fname)
        self.wrapper.send_text(self.txt_lname, lname)
        self.wrapper.send_text(self.txt_email, email)
        self.wrapper.send_text(self.txt_password, password)
        self.wrapper.send_text(self.txt_confirmpassword, confirmpassword)
        self.wrapper.click_element(self.btn_register)
