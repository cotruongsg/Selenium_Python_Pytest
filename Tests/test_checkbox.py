from selenium import webdriver
from time import sleep
import pytest
import unittest
import requests
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_Checkboxes(BaseTest):
    Assertion = unittest.TestCase()

    def test_select_checkbox(self):  
        driver = self.driver  
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Checkboxes'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'input')))
        chks = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        chks[0].click()
        chks[1].click()
        sleep(5)

        if chks[0].is_selected() and not chks[1].is_selected():
            self.Assertion.assertTrue(chks[0].is_selected,"True")
            print("Checkbox 1 is checked and Checkbox 2 is not checked.")
        else:
            self.Assertion.assertFalse("Checkbox 1 is not checked and Checkbox 2 is checked")
            






