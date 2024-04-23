from time import sleep
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts
from selenium.webdriver.common.keys import Keys
import allure

@allure.feature('CSS Testing')
class Test_CSS_Properties(BaseTest): 
    soft_asserts = SoftAsserts()

    def test_image_shifting(self):       
        driver = self.driver  
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Shifting Content'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3'))) 
        driver.find_element(By.LINK_TEXT,'Example 2: An image').click()
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.TAG_NAME,'h3'),'Shifting Content: Image'))  

        # Get the initial position
        # Option 1 to find element to check .shift css property exists or not
        # initial_image_element = driver.find_element(By.CSS_SELECTOR,'.shift')
        # if initial_image_element:
        #     initial_position = initial_image_element.value_of_css_property('left')    

        # Option 2 to find element
        initial_image_element = driver.find_element(By.CLASS_NAME,'shift')
        initial_position = initial_image_element.value_of_css_property('left')         
        print(initial_position)      

        # Click to shift the image to left 100px
        hrefs = driver.find_elements(By.TAG_NAME,'a')
        for href in hrefs:
            hf = href.get_attribute('href')
            if hf == 'https://the-internet.herokuapp.com/shifting_content/image?pixel_shift=100':
                href.click()
                break        

        sleep(3)
        # Get the final position
        final_image_position = driver.find_element(By.CLASS_NAME,'shift')
        final_left_position = final_image_position.value_of_css_property("left")
        print(final_left_position)

        #################################### Option 1 #################################
        # # Compare the positions
        # initial_left_position_int = int(initial_position.replace("px", ""))
        # final_left_position_int = int(final_left_position.replace("px", ""))        
        # shift_amount = final_left_position_int - initial_left_position_int
        # print(shift_amount)

        # # Check if the image shifted to the left by a certain number of pixels       
        # if shift_amount > 0:  # If positive, image shifted to the right            
        #     print("Image shifted to the right by", shift_amount, "pixels")
        #     self.soft_asserts.assert_false(False,'Image shifted to the right')
        # elif shift_amount < 0:  # If negative, image shifted to the left
        #     print("Image shifted to the left by", shift_amount, "pixels")
        #     self.soft_asserts.assert_true(shift_amount < 0,'Image is not shifted to the left')
        # else:  # If zero, no shift occurred
        #     print("No image shift")
        #     self.soft_asserts.assert_false(False,'No Image shift')

        #################################### Option 2 #################################
        def check_shift(shift_amount):
            return {
            shift_amount > 0: lambda: (self.soft_asserts.assert_false(False, f"Image shifted to the right by {shift_amount} pixels"), f"Image shifted to the right by {shift_amount} pixels"),
            shift_amount < 0: lambda: (self.soft_asserts.assert_true(shift_amount < 0, f"Image is not shifted to the left by {shift_amount} pixels"), f"Image shifted to the left by {shift_amount} pixels"),
            shift_amount == 0: lambda: (self.soft_asserts.assert_false(False, "No image shift"), "No image shift")
        }[True]()

        # Compare the positions
        initial_left_position_int = int(initial_position.replace("px", ""))
        final_left_position_int = int(final_left_position.replace("px", ""))        
        shift_amount = final_left_position_int - initial_left_position_int
        print(shift_amount)

        # Check if the image shifted by a certain number of pixels       
        result, message = check_shift(shift_amount)
        print(message)





