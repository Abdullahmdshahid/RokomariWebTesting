import pytest
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage


@pytest.mark.usefixtures("main")
@pytest.mark.now2
class Test_3_3():
    def test_tc_3_3(self):
        home_page = HomePage(self.chrome_webdriver)
        sign_in_page = SignInPage(self.chrome_webdriver)
        home_page.click_sign_in()
        home_page.click_sign_up()

        sign_in_page.new_sign_in()