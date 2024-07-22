from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from time import sleep


def _wait(func):
    def wrapper(*args, **kwargs):
        wait = WebDriverWait(args[0].driver, 10)
        element = visibility_of_element_located(args[1])
        wait.until(element)
        print(f"waiting for {args[1]} to load.")
        return func(*args, **kwargs)

    return wrapper


def __wait(cls):
    for key, value in cls.__dict__.items():
        if callable(value) and key != "__init__" and key != "element_is_displayed":
            setattr(cls, key, _wait(value))
    return cls


@__wait
class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, xpath):
        self.driver.find_element(*xpath).click()

    def send_text(self, xpath, text):
        self.driver.find_element(*xpath).send_keys(text)

    def select_item(self, xpath, text):
        listbox = self.driver.find_element(*xpath)
        select = Select(listbox)
        select.select_by_visible_text(text)

    def element_is_displayed(self, xpath):
        for _ in range(5):
            try:
                self.driver.find_element(*xpath).is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

