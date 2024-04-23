import pytest
from selenium import webdriver
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts

class Test_Google_Search_With_Excel(BaseTest):
    soft_asserts = SoftAsserts()

    def test_google_search_with_excel(self , get_excel_data):
        driver = self.driver
        sheet = get_excel_data       
        # Open the Google page using the url
        driver.get("https://www.google.com")

        for row in range(2, sheet.max_row + 1): # Start from 1 to skip header row

            # Find the search box by its name attribute value using find_element method
            search_box = driver.find_element(By.NAME, "q")

            # Type the search keyword and press Enter
            search_query = sheet.cell(row=row, column=1).value
            search_box.send_keys(search_query)
            search_box.send_keys(Keys.RETURN)

            # Wait for the results to load using WebDriverWait and expected_conditions
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "result-stats"))
            )

            self.soft_asserts.assert_in(search_query, self.driver.page_source)

            driver.back()

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )              
     