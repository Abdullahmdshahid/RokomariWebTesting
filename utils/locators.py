from selenium.webdriver.common.by import By

class IndexLocator():
    # SIGN IN BUTTON

    SIGN_IN_BUTTON = (By.XPATH, '//a[@href="/login"]')

    # FACEBOOK BUTTON

    FACEBOOK_BUTTON = (By.XPATH, '//*[@id="js--login-form"]/div[1]/div/button[1]')

    # GOOGLE BUTTON

    GOOGLE_BUTTON = (By.XPATH, '//*[@id="js--login-form"]/div[1]/div/button[2]')

    # USER NAME

    USER_NAME = (By.XPATH, '//input[@id="j_username"]')

    # LOGIN PASSWORD

    LOGIN_PASSWORD = (By.XPATH, '//input[@id="j_password"]')

    # LOGIN BUTTON

    LOGIN = (By.XPATH, '//*[@id="loginForm"]/button')

    # SIGN UP BUTTON

    SIGN_UP_BUTTON = (By.XPATH, '//p[text()="Sign up"]')

    # SIGN UP BY FACEBOOK

    SIGN_IN_FB = (By.XPATH, '//*[@id="js--registration-form"]/div[1]/div/button[1]')

    # SIGN UP GOOGLE

    SIGN_IN_GOOGLE = (By.XPATH, '//*[@id="js--registration-form"]/div[1]/div/button[2]')

    # FIRST NAME

    NAME = (By.ID, "nm")

    # EMAIL

    EMAIL = (By.ID, "js-email")

    # PHONE

    PHONE = (By.ID, "js-phone")

    # CREATE PASSWORD

    CREATE_PASSWORD = (By.ID, "pwd")

    PROFILE = (By.XPATH, '//span[@class="user-name"]')
    ACCOUNT = (By.XPATH, '//a[text()="My Account"]')
    CHANGE_PROFILE = (By.ID, 'js--edit-personal')
    BOOK_BUTTON = (By.XPATH, '//a[@href="/book?ref=nm"]')
    ELEC_BUTTON = (By.XPATH, '//a[@href="/electronics?ref=nm"]')
    STAI_BUTTON = (By.XPATH, '//a[@href="/stationary?ref=nm"]')
    GIFT_BUTTON = (By.XPATH, '//a[@href="/giftfinder?ref=nm"]')
    CORPO_BUTTON = (By.XPATH, '//a[@href="/corporate?ref=nm"]')
    OFFER_BUTTON = (By.XPATH, '//a[@href="/offer?ref=nm"]')
    BLOG_BUTTON = (By.XPATH, '//a[@href="https://blog.rokomari.com/?ref=nm"]')
    CHART_BUTTON = (By.XPATH, '//a[@class="cart-menu"]')
    NOTIFY_BUTTON = (By.XPATH, 'a[class*="notify"]')
    SEARCH_BUTTON = (By.XPATH, '//input[@name="term"]')
    ORDER = (By.XPATH, '//a[text()="My Orders"]')
    MY_LIST = (By.XPATH, '//a[text()="My List"]')
    CREATE_LIST = (By.XPATH, '//button[text()="Create New List"]')
    WISH_LIST = (By.XPATH, '//a[text()="My Wishlist"]')
    REVIEWS = (By.XPATH, '//a[text()="My Rating Reviews"]')
    POINT = (By.XPATH, '//a[text()="My Points"]')
    LOGOUT = (By.XPATH, '//a[@href="/logout"]')