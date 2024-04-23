from selenium import webdriver
from time import sleep
import allure
from allure_commons.types import AttachmentType
import requests
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts

@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Test Broken Image')
@allure.description('This test checks broken image.')
@allure.tag('Href testing')
@allure.label('owner','Truong Duong')
class Test_Image(BaseTest):
    soft_asserts = SoftAsserts()

    def test_broken_image(self):  
        driver = self.driver  
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Broken Images'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'img')))
        images = driver.find_elements(By.TAG_NAME,'img')

        # Iterate over each image element and check if the image is broken
        for image in images:
            # Get the source (URL) of the image
            image_url = image.get_attribute("src")
            
            # Check if the image URL is not empty
            if image_url:
                # Send a HEAD request to check the status code of the image URL
                response = requests.head(image_url)
                
                # Check if the status code indicates a broken image
                if response.status_code != 200:
                    message = f"Broken image found: {image_url}, Status code: {response.status_code}"
                    self.soft_asserts.assert_false(True, message)  # Always assert False to print the message
                    allure.attach(self.driver.get_screenshot_as_png(),name=f'{image_url}',attachment_type=AttachmentType.PNG)
        self.soft_asserts.assert_all()




