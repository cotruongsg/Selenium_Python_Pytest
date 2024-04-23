from time import sleep
import os
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts
from selenium.webdriver.common.keys import Keys


class Test_Window_Position(BaseTest):
     
    soft_asserts = SoftAsserts()
    def test_adjusting_window_position(self):
 
        # create webdriver object
        driver = self.driver 
        
        # get geeksforgeeks.org
        driver.get("https://www.geeksforgeeks.org/")
        driver.maximize_window()
        sleep(3)

        # set window position
        driver.set_window_rect(x = 100, y = 200, width = 1024, height = 700)
        sleep(3)

        print(driver.current_window_handle)

        # Get current window position
        window_position = driver.get_window_rect()
        self.soft_asserts.assert_equal(window_position['x'], 100 , 'X position is not correct')
        self.soft_asserts.assert_equal(window_position['y'], 200 , 'Y position is not correct')
        self.soft_asserts.assert_equal(window_position['width'], 1024 , 'Width position is not correct')
        self.soft_asserts.assert_equal(window_position['height'], 700 , 'Height position is not correct')
        self.soft_asserts.assert_all()

