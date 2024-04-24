import pytest
from selenium import webdriver
import os
import time
import allure
import pandas as pd
from openpyxl import load_workbook


@pytest.hookimpl(tryfirst=True)
def pytest_addoption(parser):
    # Define the command line options for pytest
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests (chrome, firefox)")
    parser.addoption("--executor", action="store", default="local", help="Executor (local, remote, standalone)")

# Get the present working directory (PWD)
pwd = os.getcwd()

# Set the path for file download
download_dir = os.path.join(pwd, 'downloads')

# Set browser options to automatically download files to the specified directory
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    # profile.default_content_setting_values.geolocation
    # 0: Deny
    # 1: Allow
    # 2: Ask (prompt for permission)
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 2
}
options.add_argument("--enable-features=AllowPopupsForUrls")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("prefs", prefs)

# The fixtures defined in conftest.py become available to all the test modules within the same directory and its subdirectories. 
# The conftest.py file acts as a local configuration file
# In this setup, the driver fixture is scoped to function, meaning that it will be initialized and cleaned up for each test function individually. 
# This ensures that each test function gets its own fresh instance of the WebDriver, allowing them to run independently of each other.
# @pytest.fixture(params=["chrome"],scope="class")
@allure.step("Open Browser")
@pytest.fixture(scope="class")
def init_driver(request):    
    browser = request.config.getoption("--browser").lower()
    executor = request.config.getoption("--executor").lower()

    # Default to Chrome and local executor if options are not specified
    if executor in ["local", "standalone", ""]:
        if browser == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
    else:
        if executor == "remote":
            command_executor = 'http://localhost:4444/wd/hub'
        else:
            command_executor = f'http://{executor}/wd/hub'  ## Expecting IP and Port. Eg. 1.1.1.1:4444

        # Create desired capabilities based on browser
        capabilities = {'browserName': browser}

        driver = webdriver.Remote(
            command_executor=command_executor,
            desired_capabilities=capabilities)

    request.cls.driver = driver
    driver.implicitly_wait(10) 
    driver.maximize_window()  
    yield driver
    driver.quit()

# Allure function
@pytest.fixture(autouse=True)
def allure_logs(request, open_browser):
    driver = open_browser
    yield driver
    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass # just ignore

# Read Excel data
@pytest.fixture(scope='class')
def get_excel_data():
    workbook = load_workbook(filename='D:\\SeleniumPOM\\Data\\SearchContents.xlsx')
    sheet = workbook.active
    return sheet

# Skip dependent function if previous function is failed
def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item
 
def pytest_runtest_setup(item):
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.xfail("previous test failed (%s)" % previousfailed.name)






   