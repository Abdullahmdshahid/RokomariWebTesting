import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account import ChangeProfilePage


@pytest.mark.usefixtures("main")
@pytest.mark.n3
class Test_4_1():
    def test_tc_4_1(self):
        home_page = HomePage(self.chrome_webdriver)
        home_page.click_login_button()
        login_page = LoginPage(self.chrome_webdriver)
        login_page.login_with_email_and_password()
        home_page.click_my_profile()
        home_page.click_my_account()
        profile_page = ChangeProfilePage(self.chrome_webdriver)
        profile_page.change_profile()
