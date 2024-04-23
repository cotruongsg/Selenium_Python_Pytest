from time import sleep
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts
from selenium.webdriver.common.keys import Keys


class Test_Mouse(BaseTest): 
    soft_asserts = SoftAsserts()

    def test_mouse_hover(self):       
        driver = self.driver  
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Hovers'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3'))) 
        divs = driver.find_elements(By.CLASS_NAME,'figure')        
        user_number = 1  # Initialize the user number counter
        action = ActionChains(driver)        
        for div in divs:
            action.move_to_element(div).perform()
            figCaption = div.find_element(By.CLASS_NAME,'figcaption')
            name = figCaption.find_element(By.TAG_NAME,'h5').text
            href = figCaption.find_element(By.TAG_NAME,'a').get_attribute('href') 
            print(name , href)
            self.soft_asserts.assert_true(name == f'name: user{user_number}' and href == f'https://the-internet.herokuapp.com/users/{user_number}', 'The name and href for the user must be the same')
            user_number += 1  # Increment the user number counter for the next iteration
            sleep(5)
        self.soft_asserts.assert_all()





            

