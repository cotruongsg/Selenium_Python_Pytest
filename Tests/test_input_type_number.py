from time import sleep
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts
from selenium.webdriver.common.keys import Keys


class Test_Input(BaseTest): 
    soft_asserts = SoftAsserts()

    def test_input_number_type(self):               
        driver = self.driver  
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Inputs'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3'))) 

        ################################ Way 1 ################################
        input = driver.find_element(By.CSS_SELECTOR,'input[type="number"]')
        input.send_keys('1')
        sleep(1)

        ################################ Way 2 ################################
        # Execute JavaScript to set the value attribute
        driver.execute_script("arguments[0].value = '123'", input)
        sleep(1)

        ################################ Way 3 ################################
        for i in range(3):
            input.send_keys(Keys.ARROW_UP)
            sleep(1)

        for i in range(3):
            input.send_keys(Keys.ARROW_DOWN) 
            sleep(1)  

        ################################ Way 4 ################################
        # Use ActionChains to simulate pressing the arrow up key
        action = ActionChains(driver)
        for i in range(5):
            action.move_to_element(input).click().send_keys(Keys.ARROW_UP).perform()
            sleep(1)