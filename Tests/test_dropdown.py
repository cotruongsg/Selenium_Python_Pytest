from selenium import webdriver
from time import sleep
import pytest
import unittest
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts

class Test_Dropdown_Menu(BaseTest):
    soft_asserts = SoftAsserts()

    def test_right_click_menu(self):  
        driver = self.driver  
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Dropdown'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3')))   

        # Create a Select object
        dropdown = driver.find_element(By.ID,'dropdown')
        select = Select(dropdown)
        
        # Now, you can interact with the dropdown using various methods of the Select class
        # For example, you can select an option by visible text, value, or index
        # Select by visible text
        select.select_by_visible_text("Option 1")
        sleep(2)
        # Get value
        selected_option = select.first_selected_option
        # Check value
        selected_value = selected_option.get_attribute('value')
        self.soft_asserts.assert_equal(selected_value, 'Option 1', 'Option 1 value is not selected')

        # Select by value
        select.select_by_value("2")
        sleep(2)

        # Select by index
        select.select_by_index(1)  # Index starts from 0
        sleep(3)

        # Get and check all values of dropdown
        expected_valued = ['Option 1', 'Option 2']
        options = [];
        for option in select.options:
            options.append(option.text)

        for option, expected_valued in zip(options, expected_valued):
            self.soft_asserts.assert_equal(option, expected_valued ,f"Option '{option}' does not match expected value '{expected_valued}'")

        




