import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("main")
@pytest.mark.now2
class Test_2_3():
    def test_tc_2_3(self):
        home_page = HomePage(self.chrome_webdriver)
        home_page.click_login_button()
        login_page = LoginPage(self.chrome_webdriver)
        login_page.login_with_email_and_password()