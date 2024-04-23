from time import sleep
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts
from selenium.webdriver.common.keys import Keys


class Test_Infinity_Scroll(BaseTest): 
    soft_asserts = SoftAsserts()

    def test_scroll_down(self):               
        driver = self.driver  
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'Infinite Scroll'))).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,'h3'))) 

        ################################ Option 1 ################################
        container = driver.find_element(By.CLASS_NAME, 'jscroll-inner')
        initial_child_divs = container.find_elements(By.CLASS_NAME, 'jscroll-added')

        # Scroll down using JavaScript
        for _ in range(5):  # Scroll down 5 times, adjust as needed
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll to the bottom of the page
            sleep(4)  # Wait for a few seconds to load content, adjust as needed
            new_child_divs = container.find_elements(By.CLASS_NAME, 'jscroll-added')
            self.soft_asserts.assert_not_equal(len(new_child_divs),len(initial_child_divs),'The new child div is not added when scroll down')
        self.soft_asserts.assert_all()

        # Refresh the page
        driver.refresh()

        # Wait for the page to be fully loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )

        ################################ Option 2 ################################
        container = driver.find_element(By.CLASS_NAME, 'jscroll-inner')
        initial_child_divs = container.find_elements(By.CLASS_NAME, 'jscroll-added')   

        # Perform a sequence of actions to scroll down
        for _ in range(5):  # Scroll down 5 times, adjust as needed
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            sleep(3)  # Wait for a few seconds to load content, adjust as needed
            new_child_divs = container.find_elements(By.CLASS_NAME, 'jscroll-added')
            self.soft_asserts.assert_not_equal(len(new_child_divs),len(initial_child_divs),'The new child div is not added when scroll down')
        self.soft_asserts.assert_all()

