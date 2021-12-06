import time

from pages.base_page import BasePage
from files.sample_data import SampleData
from utils.locators import *


class ChangeProfilePage(BasePage):

    def __init__(self, chrome_webdriver):
        super().__init__(chrome_webdriver)
        self.locator = ChangeProfileLocator

    def change_profile(self):
        change_profile_button = self.chrome_webdriver.find_element(*self.locator.CHANGE_PROFILE)
        change_profile_button.click()
        name_change = self.chrome_webdriver.find_element(*self.locator.CHANGE_NAME)
        name_change.send_keys(SampleData.book_name)
        name_change.click()
        time.sleep(5)

        birth_date = self.chrome_webdriver.find_element(*self.locator.BIRTH_DATE)
        birth_date.send_keys(SampleData.birth_date)
        birth_date.click()
        time.sleep(2)

        self.scroll_down()
        time.sleep(2)

        male = self.chrome_webdriver.find_element(*self.locator.MALE_BUTTON)
        male.click()
        time.sleep(2)

        save_button = self.chrome_webdriver.find_element(*self.locator.CHANGE_SAVE)
        save_button.click()
        self.back_to_homepage()

