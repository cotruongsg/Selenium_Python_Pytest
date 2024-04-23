from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.by import By
import time

class UserManagementPage(BasePage):

    """By locators - OR"""
    userManagement_header = (By.XPATH , "//span[@class='oxd-topbar-header-breadcrumb']/h6[contains(normalize-space(),'User Management')]")
    
    # Contructor of base class
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)