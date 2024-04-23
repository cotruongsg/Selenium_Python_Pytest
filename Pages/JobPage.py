from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.by import By
import random


class JobPage(BasePage):   

    random_number = random.randint(1, 100)
   
   
    """By locators - OR"""
    job_navigation_link = (By.XPATH , "//li[@class='oxd-topbar-body-nav-tab --parent']/span[contains(normalize-space(),'Job')]")
    job_title_link = (By.XPATH , "//ul[@class='oxd-dropdown-menu']/li/a[contains(normalize-space(),'Job Titles')]")
    job_title_label = (By.XPATH , "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']")
    add_btn = (By.XPATH , "//button[@class='oxd-button oxd-button--medium oxd-button--secondary' and contains(normalize-space(),'Add')]")
    add_job_title_label = (By.XPATH , "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title' and contains(normalize-space(),'Add Job Title')]")

    """Add Job Title page"""
    job_title_txt = (By.XPATH , "//div[@class='orangehrm-card-container']//input[@class='oxd-input oxd-input--active']")
    job_description_txt = (By.XPATH , "//div[@class='orangehrm-card-container']//textarea[contains(normalize-space(@class), 'oxd-textarea') and @placeholder = 'Type description here']")
    add_note_txt = (By.XPATH , "//div[@class='orangehrm-card-container']//textarea[contains(normalize-space(@class), 'oxd-textarea') and @placeholder = 'Add note']")
    submit_btn = (By.XPATH, "//button[@type='submit' and contains(normalize-space(),'Save')]")
    job_title_value = f'QA Automation Engineering {random_number}'   

    """Data to find in Job table"""
    new_job_added_chk = (By.XPATH , f"//div[@class='oxd-table-cell oxd-padding-cell' and normalize-space()='{job_title_value}']/preceding-sibling::div")
    new_job_delete_btn = (By.XPATH , f"//div[@class='oxd-table-cell oxd-padding-cell' and normalize-space()='{job_title_value}']/following-sibling::div[2]//i[@class='oxd-icon bi-trash']")
    new_job_confirm_delete_btn = (By.XPATH , "//button[normalize-space()='Yes, Delete']")
    job_table = (By.XPATH , "//div[@class='orangehrm-container']/div[@class='oxd-table']")

    """Data to verify"""
    new_job_deleted = (By.XPATH , f"//div[@class='oxd-table-cell oxd-padding-cell' and normalize-space()='{job_title_value}']")

    # Contructor of base class
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)