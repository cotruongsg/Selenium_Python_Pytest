import pytest
from selenium import webdriver
import os
import time
import allure
import pandas as pd
from openpyxl import load_workbook
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.remote.remote_connection import RemoteConnection
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts

load_dotenv()

@pytest.hookimpl(tryfirst=True)
def pytest_addoption(parser):
    # Define the command line options for pytest
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests (chrome, firefox)")
    parser.addoption("--executor", action="store", default="local", help="Executor (local, remote, standalone)")

# Get the present working directory (PWD)
pwd = os.getcwd()

# Set the path for file download
download_dir = os.path.join(pwd, 'downloads')

# The fixtures defined in conftest.py become available to all the test modules within the same directory and its subdirectories. 
# The conftest.py file acts as a local configuration file
# In this setup, the driver fixture is scoped to function, meaning that it will be initialized and cleaned up for each test function individually. 
# This ensures that each test function gets its own fresh instance of the WebDriver, allowing them to run independently of each other.
# @pytest.fixture(params=["chrome"],scope="class")
@allure.step("Open Browser")
@pytest.fixture(scope="class")
def init_driver(request): 
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


    browser = request.config.getoption("--browser").lower()
    executor = request.config.getoption("--executor").lower()

    if executor in ["local", "standalone", ""]:
        if browser == 'chrome':
            chrome_options = ChromeOptions()
            driver = webdriver.Chrome(options=chrome_options)
        else:
            firefox_options = FirefoxOptions()
            driver = webdriver.Firefox(options=firefox_options)
    else:
        command_executor = 'http://localhost:4444/wd/hub' if executor == "remote" else f'http://{executor}/wd/hub'

        if browser == 'chrome':
            chrome_options = ChromeOptions()
            driver = webdriver.Remote(command_executor=command_executor, options=chrome_options)
        else:
            firefox_options = FirefoxOptions()
            driver = webdriver.Remote(command_executor=command_executor, options=firefox_options)

    request.cls.driver = driver
    driver.implicitly_wait(10) 
    driver.maximize_window()  
    yield driver
    driver.quit()

# Read Excel data
@pytest.fixture(scope='class')
def get_excel_data():
    workbook = load_workbook(filename='D:\\SeleniumPOM\\Data\\SearchContents.xlsx')
    sheet = workbook.active
    return sheet

# Skip dependent function if previous function is failed
# def pytest_runtest_makereport(item, call):
#     if "incremental" in item.keywords:
#         if call.excinfo is not None:
#             parent = item.parent
#             parent._previousfailed = item
 
# def pytest_runtest_setup(item):
#     previousfailed = getattr(item.parent, "_previousfailed", None)
#     if previousfailed is not None:
#         pytest.xfail("previous test failed (%s)" % previousfailed.name)

# For Lambdatest cloud testing section

@pytest.fixture(scope='function')
def driver(request):
   
    browser = request.config.getoption("--browser").lower()
    
    username = os.getenv('LT_USERNAME', None)
    access_key = os.getenv('LT_ACCESS_KEY', None)

    selenium_endpoint = f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub"

    class_name = request.cls.__name__
    function_name = request.function.__name__
    filename = request.node.fspath.basename

    # Set the build name dynamically
    build_name = f"{class_name} class - {function_name} function in {filename} file"

    # Configure Selenium capabilities with the dynamic build name
    chrome_caps = {
        "build": build_name,
        "name": f"Testing {class_name} class - {function_name} function",
        "platform": "Windows 10",
        "browserName": "Chrome",
        "version": "latest"
    }

    firefox_caps = {
        "build": build_name,
        "name": f"Testing {class_name} - {function_name} function",
        "platform": "Windows 10",
        "browserName": "Firefox",
        "version": "latest"
    }

    edge_caps = {
        "build": build_name,
        "name": f"Testing {class_name} - {function_name} function",
        "platform": "Windows 10",
        "browserName": "Edge",
        "version": "latest"
    }

    """
    Initialize Driver For Selenium Grid On LambdaTest    
    """
   
    if browser == 'chrome' :
        options = ChromeOptions()
        options.set_capability("LT:Options", chrome_caps)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_capability("LT:Options", firefox_caps)
    elif browser == "edge":
        options = EdgeOptions()
        options.set_capability("LT:Options", edge_caps)

    # Instantiate Remote WebDriver with the corrected 'options' parameter
    driver = webdriver.Remote(
        command_executor=RemoteConnection(selenium_endpoint),
        options=options  # Corrected usage
    )

    request.cls.driver = driver

    yield driver  # Fixture teardown point

    def fin():
        # Safely check if 'rep_call' is set
        rep_call = getattr(request.node, "rep_call", None)

        # Determine test status based on 'rep_call'
        if rep_call and rep_call.failed:
            status = "failed"
        else:
            status = "passed"  # Default to "passed" if no failure indication
        # Mark the test status on LambdaTest based on result
        driver.execute_script(f"lambda-status={status}")
        driver.quit()  # Quit the driver when done

    request.addfinalizer(fin)  # Add finalizer to ensure proper cleanup


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Set a report attribute for each phase of a call (setup, call, teardown)
    setattr(item, "rep_" + rep.when, rep)

    # Ensure 'rep_call' is set during the 'call' phase
    if rep.when == "call":
        item.rep_call = rep  # Explicitly set 'rep_call' for accurate teardown logic








   