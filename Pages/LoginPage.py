from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):

    """By locators - OR"""
    username_txt = (By.NAME,"username")
    password_txt = (By.NAME,"password")
    login_btn = (By.XPATH,"//button[contains(@class, 'oxd-button--main orangehrm-login-button')]")

    # Contructor of base class
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # Page Actions
    def do_login(self, username, password):
        self.do_send_keys(self.username_txt,username)
        self.do_send_keys(self.password_txt,password)
        self.do_click(self.login_btn)
        time.sleep(8)

    # Check Title
    def getTitle(self):
        return self.get_title()
