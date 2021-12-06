import pytest

from pages.home_page import HomePage


@pytest.mark.usefixtures("main")
@pytest.mark.now
class Test_1():
    def test_tc_001(self):
        home_page = HomePage(self.chrome_webdriver)
        a = home_page.chrome_webdriver.current_url
        assert "https://www.rokomari.com/book" == a