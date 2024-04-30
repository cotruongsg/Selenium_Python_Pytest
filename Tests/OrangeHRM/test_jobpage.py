import pytest
import sys
sys.path.append('D:\\SeleniumPOM')
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.JobPage import JobPage
from Pages.UserManagementPage import UserManagementPage
from Tests.BaseTest import BaseTest
import unittest
import random
import allure

# @pytest.mark.skip
# @pytest.mark.regression
@allure.story('Job page of ORANGEHRM testing')
class Test_Add_Job(BaseTest):
    Assertion = unittest.TestCase()  
   
    # @pytest.mark.run(order=3)
    def test_add_job(self):
        # Create instance for each page
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.basePage = BasePage(self.driver)
        self.jobPage = JobPage(self.driver)    
        self.userManagementPage = UserManagementPage(self.driver)

        # Login and navigate to Admin Page
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)   
        self.basePage.do_click(self.homePage.admin_link)
        self.basePage.wait_for_element_located(self.userManagementPage.userManagement_header)

        # Navigate to Job Title Page and Add Job
        self.basePage.do_click(self.jobPage.job_navigation_link)
        self.basePage.do_click(self.jobPage.job_title_link)
        self.basePage.wait_for_element_located(self.jobPage.job_title_label)
        self.basePage.do_click(self.jobPage.add_btn)
        self.basePage.wait_for_element_located(self.jobPage.add_job_title_label)

        # Fill out the information of new job     

        self.basePage.do_send_keys(self.jobPage.job_title_txt, self.jobPage.job_title_value)
        self.basePage.do_send_keys(self.jobPage.job_description_txt, "This is a job for Software Automation Testing")
        self.basePage.do_send_keys(self.jobPage.add_note_txt,"Urgent Hiring")
        self.basePage.do_click(self.jobPage.submit_btn)
        self.basePage.wait_for_element_located(self.jobPage.job_table)

        # Delete new job added
    
        self.basePage.do_click(self.jobPage.new_job_added_chk)
        self.basePage.do_click(self.jobPage.new_job_delete_btn)
        self.basePage.wait_for_element_located(self.jobPage.new_job_confirm_delete_btn)
        self.basePage.do_click(self.jobPage.new_job_confirm_delete_btn)
        self.basePage.wait_for_element_located(self.jobPage.job_table)

        # Verify the job is deleted  
        element = self.basePage.check_element_exists(self.jobPage.new_job_deleted)

        if (element):                
            # If the element is found, fail the test
            self.fail("The job is not deleted and delete job function does not work.")
        else:       
            # If the element is not found, the test passes
            self.Assertion.assertTrue(True, "The job is deleted. Verification successful.")

        # Log out      
        self.homePage.do_logout()    
