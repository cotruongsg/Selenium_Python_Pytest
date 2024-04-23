import pytest
import os
import sys
sys.path.append(os.getcwd())
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Tests.BaseTest import BaseTest
import unittest
import inspect
import allure

# @pytest.mark.skip
# @pytest.mark.smoke
@allure.epic('Login Testing')
class Test_Login(BaseTest):
    Assertion = unittest.TestCase()       
   
    # @pytest.mark.run(order=2)
    def test_check_title(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        actual_title = self.loginPage.getTitle()
        print(actual_title)
        self.Assertion.assertEqual(actual_title,TestData.HOMEPAGE_TITLE,"The current title is not matching with the expected result is OrangeHRM")
        self.homePage = HomePage(self.driver)
        self.homePage.do_logout()
