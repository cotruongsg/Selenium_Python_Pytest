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

    def test_jquery_menu(self):                   
        driver = self.driver 
        self.basePage = BasePage(driver)    
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'JQuery UI Menus'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3'))) 

        action = ActionChains(driver)

        # Find the menu item labeled "Enabled" and click on it to expand the submenu
        main_menu = driver.find_element(By.ID, 'menu')
        menu_item = main_menu.find_element(By.XPATH, "//li[@id='ui-id-3']")
        enabled_item = menu_item.find_element(By.XPATH, '//a[contains(text(), "Enabled")]')
        action.move_to_element(enabled_item).click().perform()
        sleep(2)

        # Wait for the submenu to become visible
        submenu = menu_item.find_element(By.XPATH, "//li[@id='ui-id-4']/a[contains(text(),'Download')]")
        action.move_to_element(submenu).click().perform()
        sleep(2)

        # Find the specific submenu item (e.g., "PDF") and click on it
        pdf_submenu_item = menu_item.find_element(By.XPATH, "//a[contains(text(), 'PDF')]")
        action.move_to_element(pdf_submenu_item).click().perform()       

        # Verify that the file has been downloaded to the specified directory
        file_name = "menu.pdf"  # Provide the expected file name

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
        file = self.basePage.wait_for_file(completed_file_download_path,60,1)  
        if file:
            self.soft_asserts.assert_true(os.path.exists(completed_file_download_path),"File is downloaded unsuccessfully")
            self.soft_asserts.assert_all()
