from selenium.webdriver.common.by import By

class IndexLocator():
    # SIGN IN BUTTON

    SIGN_IN_BUTTON = (By.XPATH, '//a[@href="/login"]')

    # FACEBOOK BUTTON

    FACEBOOK_BUTTON = (By.XPATH, '//*[@id="js--login-form"]/div[1]/div/button[1]')

    # GOOGLE BUTTON

    GOOGLE_BUTTON = (By.XPATH, '//*[@id="js--login-form"]/div[1]/div/button[2]')

    # LOGIN BUTTON

    LOGIN = (By.XPATH, '//*[@id="loginForm"]/button')

    # SIGN UP BUTTON

    SIGN_UP_BUTTON = (By.XPATH, '//p[text()="Sign up"]')

    # SIGN UP BY FACEBOOK

    SIGN_FB = (By.XPATH, '//*[@id="js--registration-form"]/div[1]/div/button[1]')

    # SIGN UP GOOGLE

    SIGN_GOOGLE = (By.XPATH, '//*[@id="js--registration-form"]/div[1]/div/button[2]')

    # FIRST NAME

    NAME = (By.ID, "nm")

    # EMAIL

    EMAIL = (By.ID, "js-email")

    # PHONE

    PHONE = (By.ID, "js-phone")

    # PASSWORD

    PASSWORD = (By.ID, "pwd")