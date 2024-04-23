#Using maxfail command-line operation to stop test suite after n test failure using Selenium test automation in Python with pytest 
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
 
# If we want to stop test suite after n test failure using pytest -rx --verbose --capture=no --maxfail=2
@pytest.mark.incremental # Stop Test Suite after N Test Failures in Pytest
class Test_Scenario_1(BaseTest):
    def test_1(self):
        self.driver.get('https://www.lambdatest.com/blog/')
        self.driver.maximize_window()
 
        expected_title = "LambdaTest Blogs"
        assert expected_title ==  self.driver.title
        time.sleep(5)
 
    def test_2(self):
        self.driver.get('https://www.google.com/')
        self.driver.maximize_window()
        title = "Google"
        assert title == self.driver.title
 
        search_text = "LambdaTest"
        search_box = self.driver.find_element(By.XPATH, "//input[@name='q']")
        search_box.send_keys(search_text)
 
        time.sleep(5)
        search_box.submit()
 
        time.sleep(5)
        
        # Click on the LambdaTest HomePage Link
        # This test will fail as the titles will not match
        title = "Cross Browser Testing Tools | Free Automated Website Testing | LambdaTest_1"
        lt_link = self.driver.find_element(By.XPATH,"//h3[.='LambdaTest: Cross Browser Testing Tools | Free Automated ...']")
        lt_link.click()
 
        time.sleep(10)
        assert title == self.driver.title   
        time.sleep(2)
 
    def test_3(self):
        self.driver.get('https://www.lambdatest.com/')
        self.driver.maximize_window()
 
        expected_title = "Next-Generation Mobile Apps and Cross Browser Testing Cloud | LambdaTest"
        assert expected_title ==  self.driver.title
        time.sleep(5)
 

@pytest.mark.incremental
class Test_Scenario_2(BaseTest):
    def test_4(self):
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        self.driver.maximize_window()
 
        self.driver.find_element(By.NAME,"li1").click()
        self.driver.find_element(By.NAME,"li2").click()
 
        title = "Sample page - lambdatest.com"
        assert title ==  self.driver.title
 
        sample_text = "Happy Testing at LambdaTest"
        email_text_field =  self.driver.find_element(By.ID,"sampletodotext")
        email_text_field.send_keys(sample_text)
        time.sleep(5)
 
        self.driver.find_element(By.ID,"addbutton").click()
        time.sleep(5)
 
        assert self.driver.find_element(By.XPATH,"//span[.='Happy Testing at LambdaTest']").text == sample_text  