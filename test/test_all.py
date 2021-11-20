import time

import pytest
from selenium.webdriver.common.keys import Keys
# from tests.base_test import BaseTestClass
from pages.index import Index

@pytest.mark.usefixtures("main")
class Test():

    def test_tc_001(self):
        index = Index(self.chrome_webdriver)
        a = index.chrome_webdriver.current_url
        assert "https://www.rokomari.com/book" == a
