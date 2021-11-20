from pages.locators import *


class Index():

    def __init__(self, chrome_webdriver):
        self.chrome_webdriver = chrome_webdriver
        self.locator = IndexLocator

    def sign_in(self):
        return self.chrome_webdriver.find_element(*self.locator.SIGN_IN_BUTTON)

    def facebook_button(self):
        return self.chrome_webdriver.find_element(*self.locator.FACEBOOK_BUTTON)

    def google_button(self):
        return self.chrome_webdriver.find_element(*self.locator.GOOGLE_BUTTON)

    def login(self):
        return self.chrome_webdriver.find_element(*self.locator.LOGIN)

    def sign_up(self):
        return self.chrome_webdriver.find_element(*self.locator.SIGN_UP_BUTTON)

    def sign_in_fb(self):
        return self.chrome_webdriver.find_element(*self.locator.SIGN_IN_FB)

    def sign_in_google(self):
        return self.chrome_webdriver.find_element(*self.locator.SIGN_IN_GOOGLE)

    def name(self):
        return self.chrome_webdriver.find_element(*self.locator.NAME)

    def email(self):
        return self.chrome_webdriver.find_element(*self.locator.EMAIL)

    def phone(self):
        return self.chrome_webdriver.find_element(*self.locator.PHONE)

    def password(self):
        return self.chrome_webdriver.find_element(*self.locator.PASSWORD)

    def profile(self):
        return self.chrome_webdriver.find_element(*self.locator.PROFILE)

    def account(self):
        return self.chrome_webdriver.find_element(*self.locator.ACCOUNT)

    def change_profile(self):
        return self.chrome_webdriver.find_element(*self.locator.CHANGE_PROFILE)

    def book_button(self):
        return self.chrome_webdriver.find_element(*self.locator.BOOK_BUTTON)

    def elec_button(self):
        return self.chrome_webdriver.find_element(*self.locator.ELEC_BUTTON)

    def stai_button(self):
        return self.chrome_webdriver.find_element(*self.locator.STAI_BUTTON)

    def gift_button(self):
        return self.chrome_webdriver.find_element(*self.locator.GIFT_BUTTON)

    def corpo_button(self):
        return self.chrome_webdriver.find_element(*self.locator.CORPO_BUTTON)

    def offer_button(self):
        return self.chrome_webdriver.find_element(*self.locator.OFFER_BUTTON)

    def blog_button(self):
        return self.chrome_webdriver.find_element(*self.locator.BLOG_BUTTON)

    def chart_button(self):
        return self.chrome_webdriver.find_element(*self.locator.CHART_BUTTON)

    def notify_button(self):
        return self.chrome_webdriver.find_element(*self.locator.NOTIFY_BUTTON)

    def search_button(self):
        return self.chrome_webdriver.find_element(*self.locator.SEARCH_BUTTON)

    def order(self):
        return self.chrome_webdriver.find_element(*self.locator.ORDER)

    def my_list(self):
        return self.chrome_webdriver.find_element(*self.locator.MY_LIST)

    def create_list(self):
        return self.chrome_webdriver.find_element(*self.locator.CREATE_LIST)

    def wish_list(self):
        return self.chrome_webdriver.find_element(*self.locator.WISH_LIST)

    def reviews(self):
        return self.chrome_webdriver.find_element(*self.locator.REVIEWS)

    def point(self):
        return self.chrome_webdriver.find_element(*self.locator.POINT)

    def logout(self):
        return self.chrome_webdriver.find_element(*self.locator.LOGOUT)
