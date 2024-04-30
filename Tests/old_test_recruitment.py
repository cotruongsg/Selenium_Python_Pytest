from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# # Assuming you have already initialized the WebDriver (e.g., ChromeDriver)
# driver = webdriver.Chrome()

# # Replace 'your_url' with the actual URL of the page you want to open
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# time.sleep(5)

# driver.find_element(By.NAME,'username').send_keys('admin')
# driver.find_element(By.NAME,'password').send_keys('admin123')
# driver.find_element(By.XPATH,"//button[contains(@class, 'oxd-button--main orangehrm-login-button')]").click()
# time.sleep(5)

# # Replace 'your_div_id' with the actual ID of the div you want to inspect
# rec = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and contains(text(),'Recruitment')]")
# rec.click()
# time.sleep(5)

# # parent div
# parent_div = driver.find_element(By.XPATH, "//div[@class='oxd-select-dropdown --position-bottom']")

# # Get all child elements of the parent div
# child_elements = parent_div.find_elements(By.XPATH, '*')

# # Loop through the child elements and print their details
# for child in child_elements:
#     tag_name = child.tag_name
#     text = child.text
#     attributes = child.get_property('attributes')

#     print(f'Tag Name: {tag_name}, Text: {text}, Attributes: {attributes}')

# # Close the browser window
# driver.quit()