from pytest import mark
from utilites.excel_lib import get_data,get_header

class TestRegistration:
    headers = get_header("smoke", "test_registration")
    test_data = get_data("smoke", "test_registration")

    @mark.parametrize(headers,test_data)
    def test_register(self, pages,gender,fname,lname,email,password,confirmpassword):
        pages.homepage.click_registration()
        pages.registration.register_user(pages,gender,fname,lname,email,password,confirmpassword)