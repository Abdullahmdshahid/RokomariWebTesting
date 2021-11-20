import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope='class')
def main(request):
    chrome_webdriver = webdriver.Chrome(executable_path=r"\RokomariWebTest\ChromeDriver\chromedriver.exe")
    chrome_webdriver.get("https://www.rokomari.com/book")
    chrome_webdriver.maximize_window()
    action = ActionChains(chrome_webdriver)
    request.cls.chrome_webdriver = chrome_webdriver
    yield
    chrome_webdriver.close()