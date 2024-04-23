from time import sleep
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts
import os

class Test_Download(BaseTest): 
    soft_asserts = SoftAsserts()

    def test_file_download(self):       
        driver = self.driver  
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'File Upload'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3'))) 
        file_input = driver.find_element(By.ID,'file-upload')     
        file_input.send_keys('D:\\SeleniumPOM\\Tests\\downloads\\test.txt')         
        sleep(2)
        # Click the submit button
        driver.find_element(By.ID, 'file-submit').click()
        sleep(3)

        ############################# Check Uploaded File #############################       
        confirmation = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME, 'h3')))
        file_uploaded = driver.find_element(By.ID,'uploaded-files')
        self.soft_asserts.assert_true(confirmation.text == 'File Uploaded!' and file_uploaded.text == 'test.txt','File did not upload successfully')
        self.soft_asserts.assert_all()





