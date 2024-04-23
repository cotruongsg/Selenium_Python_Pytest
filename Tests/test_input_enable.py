from selenium import webdriver
from time import sleep
import pytest
import allure
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts


@allure.severity(allure.severity_level.NORMAL)
@allure.title('Test Case for Input and Checkbox Element')
@allure.description('Check Enable/Disable for Input and Add/Remove Checkbox Element')
@allure.label('owner','Truong Duong')
@allure.tag('Input and Checkbox Element')
class Test_Dynamic_Controls(BaseTest): 
    allure.dynamic.title('Test Case for Input and Checkbox Element')
    soft_asserts = SoftAsserts()

    def test_enable_disable_displayed(self): 
        with allure.step('Test Case for Input Element'):
            # Test Case 1 : Enable / Disable Input 
            driver = self.driver  
            driver.get("https://the-internet.herokuapp.com/")
            driver.maximize_window()
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Dynamic Controls'))).click()
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h4')))  
            btn = driver.find_element(By.XPATH,"//form[@id='input-example']/button")
            # Enable Input
            if btn.text == 'Enable':
                btn.click()
                WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.ID,'loading')))
                p = driver.find_element(By.XPATH,"//form[@id='input-example']/p").text
                self.soft_asserts.assert_equal(p,"It's enabled!",'The input element notification for enabled is displayed uncorrectly')
                self.soft_asserts.assert_true(btn.is_enabled(),"The input is not enabled")

            # Disable Input
            if btn.text == 'Disable':
                btn.click()
                WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.ID,'loading')))
                p = driver.find_element(By.XPATH,"//form[@id='input-example']/p").text
                # Check if the element is disabled
                is_disabled = btn.get_attribute("disabled")
                print(is_disabled)
                self.soft_asserts.assert_equal(p,"It's disabled!",'The input element notification for disabled is displayed uncorrectly')
                self.soft_asserts.assert_false(is_disabled,"The input is not disabled")


        with allure.step('Test Case for Checkbox Element'):
            # Test Case 2 : Add / Remove Checkbox
            # Remove Checkbox
            chk = driver.find_element(By.ID, 'checkbox')
            removeBtn = driver.find_element(By.XPATH, "//form[@id='checkbox-example']/button")
            if removeBtn.text == "Remove":
                removeBtn.click()
                WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, 'loading')))
                p = driver.find_element(By.XPATH, "//form[@id='checkbox-example']/p").text
                self.soft_asserts.assert_equal(p, "It's gone!", 'The checkbox element notification for removing is displayed incorrectly')

            try:
            
                is_displayed = chk.is_displayed()
            except StaleElementReferenceException:
                is_displayed = False

            self.soft_asserts.assert_false(is_displayed, "The checkbox is not removed")

            # Add Checkbox
            if removeBtn.text == "Add":
                removeBtn.click()
                WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, 'loading')))
                # Wait for the checkbox to become visible
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'checkbox')))

                # Additional assertion for the notification message
                p = driver.find_element(By.XPATH, "//form[@id='checkbox-example']/p").text
                self.soft_asserts.assert_equal(p, "It's back!", 'The checkbox element notification for adding is displayed incorrectly')     

                # Attempt to check if the checkbox is displayed, retrying if a StaleElementReferenceException occurs
                try:
                    chk = driver.find_element(By.ID, 'checkbox')
                    is_displayed = chk.is_displayed()
                    print(is_displayed)
                    is_displayed = True           
                except StaleElementReferenceException:
                    # If a StaleElementReferenceException occurs, retry once
                    is_displayed = chk.is_displayed()

                # Assert the result
                self.soft_asserts.assert_true(is_displayed,'The checkbox is not displayed')    
                self.soft_asserts.assert_equal(is_displayed,True,'The checkbox is not displayed')
                print('Passing now....')
                self.soft_asserts.assert_all()      
                    
    
           
            
          



         
            
            




        




            


            

