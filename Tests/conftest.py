import pytest
from selenium import webdriver
import os
import time
import pandas as pd
from openpyxl import load_workbook

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
@pytest.fixture(params=["chrome"],scope="class")
def init_driver(request):
    selenium_hub_url = 'http://localhost:4444/wd/hub'
    if request.param.lower() == "chrome":
        # web_driver = webdriver.Chrome(options=options)
        web_driver = webdriver.Remote(command_executor=selenium_hub_url, options=options)

    if request.param.lower() == "firefox":
        web_driver = webdriver.Firefox()

    request.cls.driver = web_driver   
    web_driver.maximize_window()  
    yield web_driver
    web_driver.quit()

# @pytest.fixture(params=["chrome", "firefox"], scope="class")
# def init_driver(request):
#     browser = request.param.lower()

#     hub_url = "http://10.0.0.53:4444/wd/hub"  # Replace <hub-ip> with your actual hub IP or hostname

#     if browser == "chrome":
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("--disable-extensions")
#         chrome_options.add_argument("--headless")  # Add other Chrome options as needed

#         capabilities = {
#             "browserName": "chrome",
#             "goog:chromeOptions": {
#                 "args": ["--disable-extensions", "--headless"]
#             },
#             "browserVersion": "100",
#             "platformName": "Windows",
#             "se:name": "My simple test",
#             "se:sampleMetadata": "Sample metadata value",
#         }

#         capabilities.update(chrome_options.to_capabilities())

#         web_driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=capabilities)
#     elif browser == "firefox":
#         capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
#         web_driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=capabilities)
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
    
#     request.cls.driver = web_driver
#     web_driver.implicitly_wait(5)
#     web_driver.maximize_window()
#     web_driver.implicitly_wait(2)

#     yield

#     web_driver.quit()

@pytest.fixture(scope='class')
def get_excel_data():
    workbook = load_workbook(filename='D:\\SeleniumPOM\\Data\\SearchContents.xlsx')
    sheet = workbook.active
    return sheet

def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item
 
def pytest_runtest_setup(item):
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.xfail("previous test failed (%s)" % previousfailed.name)






   