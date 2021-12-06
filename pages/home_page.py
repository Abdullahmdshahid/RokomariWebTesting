from selenium.webdriver import Keys

from pages.base_page import BasePage
from files.sample_data import SampleData
from utils.locators import *


class HomePage(BasePage):

    def __init__(self, chrome_webdriver):
        super().__init__(chrome_webdriver)
        self.locator = HomePageLocator

    def click_sign_in(self):
        button = self.chrome_webdriver.find_element(*self.locator.SIGN_IN_BUTTON)
        button.click()

    def click_sign_up(self):
        button = self.chrome_webdriver.find_element(*self.locator.SIGN_UP_BUTTON)
        button.click()

    def click_login_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.SIGN_IN_BUTTON)
        button.click()

    def click_my_profile(self):
        super().wait_element(*self.locator.PROFILE)
        button = self.chrome_webdriver.find_element(*self.locator.PROFILE)
        button.click()

    def click_my_account(self):
        super().wait_element(*self.locator.ACCOUNT)
        button = self.chrome_webdriver.find_element(*self.locator.ACCOUNT)
        button.click()

    def click_order(self):
        super().wait_element(*self.locator.ORDER)
        button = self.chrome_webdriver.find_element(*self.locator.ORDER)
        button.click()

    def click_list(self):
        super().wait_element(*self.locator.MY_LIST)
        button = self.chrome_webdriver.find_element(*self.locator.MY_LIST)
        button.click()

    def click_wish_list(self):
        super().wait_element(*self.locator.WISH_LIST)
        button = self.chrome_webdriver.find_element(*self.locator.WISH_LIST)
        button.click()

    def click_point(self):
        super().wait_element(*self.locator.POINT)
        button = self.chrome_webdriver.find_element(*self.locator.POINT)
        button.click()

    def logout(self):
        super().wait_element(*self.locator.LOGOUT)
        button = self.chrome_webdriver.find_element(*self.locator.LOGOUT)
        button.click()

    def search_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.SEARCH_BUTTON)
        button.send_keys(SampleData.book_name)
        button.send_keys(Keys.ENTER)
        button.click()

    def chart_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.CHART_BUTTON)
        button.click()

    def notify_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.NOTIFY_BUTTON)
        button.click()

    def book_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.BOOK_BUTTON)
        button.click()

    def elec_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.ELEC_BUTTON)
        button.click()

    def stai_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.STAI_BUTTON)
        button.click()

    def gift_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.GIFT_BUTTON)
        button.click()

    def corpo_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.CORPO_BUTTON)
        button.click()

    def offer_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.OFFER_BUTTON)
        button.click()

    def blog_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.BLOG_BUTTON)
        button.click()