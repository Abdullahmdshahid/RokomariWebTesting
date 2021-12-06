import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account import ChangeProfilePage
from pages.order_page import OrderPage


@pytest.mark.usefixtures("main")
@pytest.mark.now
class Test_4_2():

    def test_tc_4_2(self):
        home_page = HomePage(self.chrome_webdriver)
        home_page.click_login_button()
        login_page = LoginPage(self.chrome_webdriver)
        login_page.login_with_email_and_password()
        home_page.click_my_profile()
        home_page.click_order()
        order_page = OrderPage(self.chrome_webdriver)
        order_page.click_order_button()