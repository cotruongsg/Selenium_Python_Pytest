import pytest
from selenium import webdriver
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts
from Config.config import TestData


class Test_Google_Search_Using_Parametrize_Excel(BaseTest):
    soft_asserts = SoftAsserts()   

    @pytest.mark.parametrize('search_query, expected_results',  TestData.load_test_data())
    def test_google_search_with_excel_and_parametrize(self , search_query, expected_results):
        driver = self.driver
        # Open Google
        driver.get("https://www.google.com")
        
        # Find the search box and enter the search query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        
        # Check if the expected title is present in the page title
        assert expected_results in self.driver.page_source

        driver.back()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
