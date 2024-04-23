# import the libs
from selenium import webdriver
from time import sleep
import pytest
import unittest
from Tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# HTTP Basic Auth alert: The built-in HTTP standard for restricting access is known as basic authentication. In HTTP basic authentication, 
# a request is authenticated when it contains the following header field
class Test_Alert(BaseTest):
    Assertion = unittest.TestCase()

    def test_signIn(self):  
        driver = self.driver      

        driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        driver.maximize_window()
        sleep(5)

        homepage = driver.find_element(By.TAG_NAME,'p').text.strip()
        print(homepage)

        self.Assertion.assertEqual(homepage,"Congratulations! You must have the proper credentials.","Login is not successful.")

   
   


      


        

