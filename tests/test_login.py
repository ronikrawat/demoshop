from pytest import mark
from utilites.excel_lib import get_data, get_header


class TestLogin:
    headers = get_header("smoke", "test_login_positive")
    test_data = get_data("smoke", "test_login_positive")

    @mark.parametrize(headers, test_data)
    def test_login_positive(self, pages, email, password):
        pages.homepage.click_login()
        pages.loginpage.login(email, password)
        print(pages.loginpage.login_status(email))
        assert True == pages.loginpage.login_status(email), f"failed to login with {email, password}"

    test_data = get_data("smoke", "test_login_negative")

    @mark.parametrize(headers, test_data)
    def test_login_negative(self, pages, email, password):
        pages.homepage.click_login()
        pages.loginpage.login(email, password)
        print(pages.loginpage.login_status(email))
        assert False == pages.loginpage.login_status(email), f"Login with invalid details {email, password}"
