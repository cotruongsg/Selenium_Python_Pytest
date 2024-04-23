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


class Test_JQuery(BaseTest): 
    soft_asserts = SoftAsserts()

    def test_multiple_tab(self):
        driver = self.driver         
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Multiple Windows'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3'))) 
        original_tab = driver.current_window_handle        
        new_tab = None
        driver.find_element(By.LINK_TEXT,'Click Here').click()
        sleep(3)
        all_tabs = driver.window_handles
        for tab in all_tabs:
            if tab != original_tab:
                new_tab = tab
                break
        print(original_tab)
        print(new_tab)
        driver.switch_to.window(new_tab)   
        new_tab_title = driver.title
        print("Title of the new tab:", new_tab_title) 
        self.soft_asserts.assert_equal(new_tab_title,'New Window','The title of new tab is wrong')   

 





       


