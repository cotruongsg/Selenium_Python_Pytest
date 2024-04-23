from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time , os , traceback , inspect
import sys , os
from datetime import datetime
sys.path.append(os.getcwd())
from Config.config import TestData


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def do_click(self , by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self , by_locator):
        element =  WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.text
    
    def get_title(self):        
        return self.driver.title
    
    def wait_for_element_located(self, by_locator):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))

    def take_screenshot(self , classname , test_name):
        try:
            # Get the class name
            class_name = classname

            # Create a folder based on the class name if it doesn't exist
            class_folder = os.path.join(TestData.failed_folder, class_name)
            if not os.path.exists(class_folder):
                os.makedirs(class_folder)

            # Get test name
            test_name = test_name

            # Create a subfolder based on the test name if it doesn't exist
            test_folder = os.path.join(class_folder, test_name)
            if not os.path.exists(test_folder):
                os.makedirs(test_folder)

            # Get the current date and time
            current_time = datetime.now().strftime("%m-%d-%Y_%I-%M-%S-%p")      

            # Capture screenshot
            file_name = f"{test_name}_{current_time}_failed.png"        
            screenshot_path = os.path.join(test_folder, file_name)
            # print(screenshot_path)
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved")

        except Exception as e:
            print(f"Failed to take screenshot: {traceback.format_exc()}")
   
    
    def check_element_exists(self, by_locator):
        try:
            element = self.driver.find_element(by_locator)
            return element.is_displayed()
        except:
            return False
        
    def wait_for_file(self, file_path, timeout=60, interval=1):
        """
        Wait for a file to exist.

        Args:
        - file_path (str): The path to the file.
        - timeout (int): Maximum time to wait in seconds. Default is 60 seconds.
        - interval (int): Interval between checks in seconds. Default is 1 second.

        Returns:
        - bool: True if the file exists within the timeout period, False otherwise.
        """
        start_time = time.time()  # Get the start time
        timeout = int(timeout)  # Convert timeout to an integer
        while time.time() - start_time < timeout:  # Loop until the timeout is reached
            if os.path.exists(file_path):  # Check if the file exists
                return True  # Return True if the file exists
            time.sleep(interval)  # Wait for the specified interval before checking again
        return False  # Return False if the timeout is reached without finding the file