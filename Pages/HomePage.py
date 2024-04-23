from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):

    """By locators - OR"""
    profile_link = (By.XPATH , "//span[@class='oxd-userdropdown-tab']")
    logout_link = (By.XPATH , "//a[@class='oxd-userdropdown-link' and contains(text(),'Logout')]")
    admin_link = (By.XPATH , "//a[@class='oxd-main-menu-item']/span[contains(normalize-space(), 'Admin')]")

    # Contructor of base class
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # Page Actions
    def do_logout(self):
        self.do_click(self.profile_link)
        self.do_click(self.logout_link)
        time.sleep(5)
        self.driver.close()
      

  

