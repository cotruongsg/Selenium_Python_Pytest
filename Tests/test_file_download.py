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
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'File Download'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3'))) 
        driver.find_element(By.LINK_TEXT,'test.txt').click()     

        # Wait for the file to download (you may need to adjust the wait time based on file size and network speed)
        sleep(5)

        # Verify that the file has been downloaded to the specified directory
        file_name = "test.txt"  # Provide the expected file name

        # Get the present working directory (PWD)
        pwd = os.getcwd()

        # Name of the download folder
        download_folder_name = "downloads"

        # Create the download folder path by concatenating PWD and folder name
        download_folder_path = os.path.join(pwd, download_folder_name)

        # Check if the download folder exists, if not, create it
        if not os.path.exists(download_folder_path):
            os.makedirs(download_folder_path)
        completed_file_download_path = os.path.join(download_folder_path,file_name)       
        
        self.soft_asserts.assert_true(os.path.exists(completed_file_download_path),"File is downloaded unsuccessfully")
        self.soft_asserts.assert_all()
            
    

        