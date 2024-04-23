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
import allure


@allure.label('owner','Suong')
class Test_JQuery(BaseTest): 
    soft_asserts = SoftAsserts()

    def test_jquery_menu(self):                   
        driver = self.driver        
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Key Presses'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3'))) 
      
        input = driver.find_element(By.ID,'target')

        # Define a list of keys to simulate
        keys_data = [
            ("TAB", Keys.TAB),
            ("BACK_SPACE", Keys.BACKSPACE),
            ('DELETE', Keys.DELETE),           
            ("ESCAPE", Keys.ESCAPE),
            ("SHIFT", Keys.SHIFT),
            ("ALT", Keys.ALT),
            ("CONTROL", Keys.CONTROL),
            ("UP", Keys.ARROW_UP),
            ("DOWN", Keys.ARROW_DOWN),
            ("LEFT", Keys.ARROW_LEFT),
            ("RIGHT", Keys.ARROW_RIGHT),
            ("SPACE", Keys.SPACE)
        ]

        # Loop through the list of keys and send them to the input field
        for key_name, key in keys_data:
            input.click() 
            input.send_keys(key)        
            result = driver.find_element(By.ID,'result').text
            self.soft_asserts.assert_equal(result,f'You entered: {key_name}', f'{key_name} pressed is displayed uncorrectly in result field')
        self.soft_asserts.assert_all()

