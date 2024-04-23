# import the libs
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
from selenium.webdriver.common.keys import Keys


@allure.id('1')
class Test_IFRAME(BaseTest):
    Assertion = unittest.TestCase()

    def test_add_content(self):
        driver = self.driver 
       
        # go to the home page
        driver.get('https://the-internet.herokuapp.com/iframe')

        # wait for page to load completely
        driver.maximize_window()
        sleep(5)

        # Switch to iframe option 1
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'mce_0_ifr')))

        driver.find_element(By.TAG_NAME, 'p').clear()
        driver.find_element(By.TAG_NAME, 'p').send_keys('Hello World')

        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

        driver.switch_to.default_content()
        driver.find_element(By.XPATH, '//button[@title="Bold"]').click()

        sleep(3)      

        # Switch to the iframe option 2
        iframe = driver.find_element(By.ID, 'mce_0_ifr')
        driver.switch_to.frame(iframe)

        updatedHTML = driver.find_element(By.TAG_NAME, 'p').get_attribute("innerHTML")
        print(updatedHTML)

        if "<strong>" in updatedHTML:
            bold = driver.find_element(By.TAG_NAME, 'strong').value_of_css_property('font-weight')            
            if bold in ['bold', 'bolder', '700', '800', '900']:
                assert True, "Text is bold"
            else:
                assert False, "Text is not bold"
        else:
            assert False, "NO STRONG TAG EXISTS"

       

