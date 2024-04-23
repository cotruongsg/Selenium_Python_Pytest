from time import sleep
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts
from selenium.webdriver.common.keys import Keys
import allure

@allure.label('owner','Truong')
class Test_Slider(BaseTest): 
    soft_asserts = SoftAsserts()

    def test_horizontal_slider(self):       
        driver = self.driver  
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Horizontal Slider'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3'))) 

        # Find the slider element
        slider = driver.find_element(By.XPATH,"//input[@type='range']")

        # Click on the slider to set focus
        slider.click()
        sleep(3)

        # Use arrow keys to move the slider right (increase value)
        for _ in range(10):
            slider.send_keys(Keys.ARROW_RIGHT)
            sleep(0.5)  # Add a delay for demonstration        

        # Use arrow keys to move the slider left (decrease value)
        for _ in range(10):
            slider.send_keys(Keys.ARROW_LEFT)
            sleep(0.5)  # Add a delay for demonstration

        sleep(3)
        
        # Alternatively, click and drag the slider with mouse
        action = ActionChains(driver)
        action.click_and_hold(slider).move_by_offset(50, 0).release().perform()
        sleep(2)  # Add a delay for demonstration


