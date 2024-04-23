from time import sleep
import os
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts
from selenium.webdriver.common.keys import Keys
from Pages.BasePage import BasePage
import allure
from Tests.BaseTest import BaseTest


class Test_Keys_Down(BaseTest):

    def test_keys_down(self): 
        # create webdriver object
        driver = self.driver        
        
        # get geeksforgeeks.org
        driver.get("https://www.geeksforgeeks.org/")
        
        # create action chain object
        action = ActionChains(driver)
        
        # perform the operation
        action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()

        sleep(3)
       