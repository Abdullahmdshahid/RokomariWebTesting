from pages.base_page import BasePage
from utils.locators import *


class OrderPage(BasePage):

    def __init__(self, chrome_webdriver):
        super().__init__(chrome_webdriver)
        self.locator = HomePageLocator

    def click_order_button(self):
        self.back_to_homepage()