from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from files.sample_data import SampleData
from utils.locators import *


class LoginPage(BasePage):

    def __init__(self, chrome_webdriver):
        super().__init__(chrome_webdriver)
        self.locator = LoginPageLocator

    def login_with_email_and_password(self):
        email_txtbox = self.chrome_webdriver.find_element(*self.locator.USER_NAME)
        password_txtbox = self.chrome_webdriver.find_element(*self.locator.LOGIN_PASSWORD)
        email_txtbox.send_keys(SampleData.name)
        password_txtbox.send_keys(SampleData.password)
        self.chrome_webdriver.implicitly_wait(10)
        submit_button = self.chrome_webdriver.find_element(*self.locator.LOGIN)
        log_in = submit_button
        action = ActionChains(self.chrome_webdriver)
        action.move_to_element_with_offset(log_in, 5, 5)
        action.click()
        action.perform()
