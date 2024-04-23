from selenium import webdriver
from time import sleep
import pytest
import unittest
import allure
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@allure.label('owner','Truong Duong')
class Test_Context_Click(BaseTest):
    Assertion = unittest.TestCase()

    def test_right_click_menu(self):  
        driver = self.driver  
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Context Menu'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3')))
        action = ActionChains(driver)
        hotSpot = driver.find_element(By.ID, "hot-spot")
        action.context_click(hotSpot).perform()
        sleep(2)
        alert = driver.switch_to.alert
        print(alert.text)
        self.Assertion.assertEqual(alert.text, "You selected a context menu", "Wrong message of alert")
        alert.accept()
        sleep(2)

