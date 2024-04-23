from selenium import webdriver
from time import sleep
import pytest
import unittest
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Test_Drag_Drop(BaseTest):
    Assertion = unittest.TestCase()

    def test_drag_drop_item(self):  
        driver = self.driver  
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Drag and Drop'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3')))        
        source_element = driver.find_element(By.ID,"column-a")
        target_element = driver.find_element(By.ID,"column-b")
        action = ActionChains(driver)
        action.drag_and_drop(source_element,target_element).perform()
        sleep(5)
        new_target_element = driver.find_element(By.TAG_NAME,"header").text
        self.Assertion.assertEqual(new_target_element,'A','Drag and Drop is not supported')