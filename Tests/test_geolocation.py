from time import sleep
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts
import os

class Test_Gelocation(BaseTest): 
    soft_asserts = SoftAsserts()

    def test_geolocation_allow_permission(self):       
        driver = self.driver  
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Geolocation'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3'))) 
        driver.find_element(By.TAG_NAME,'button').click()
        sleep(5)
        latitude = driver.find_element(By.ID, 'lat-value').text
        longitude = driver.find_element(By.ID, 'long-value').text
        expected_latitude_prefix = '37'
        expected_longitude_prefix = '-121'
        self.soft_asserts.assert_true(latitude.startswith(expected_latitude_prefix) and longitude.startswith(expected_longitude_prefix), 'The latitude and longitude functions work incorrectly')
        self.soft_asserts.assert_all()
