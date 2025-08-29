from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open Amazon home page
url = "https://www.amazon.com/"
driver.get(url)
# Get to login page by clicking the signin button
sleep(4)
# sign_in_button
driver.find_element(By.ID, "nav-link-accountList").click()
sleep(3)

#  Creating Locators
# amazon_logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']").click()
sleep(4)
driver.back()
sleep(4)
# email_field
driver.find_element(By.ID, "ap_email_login").send_keys("washingtonosha209@yahoo.com")
#continue_button
driver.find_element(By.XPATH, "//input[@type='submit']").click()
# conditions_of_use
driver.find_element(By.XPATH, "//p[@class='a-spacing-top-medium a-size-small legal-text']//a[(text()='Conditions of Use')]").click()
# privacy_notice_link
driver.find_element(By.XPATH, "//p[@class='a-spacing-top-medium a-size-small legal-text']//a[(text()='Privacy Notice')]").click()
# Need Help?
driver.find_element(By.XPATH, "//a[normalize-space()='Need help?']").click()
# forgot_password
driver.find_element(By.ID, "//a[@id='auth-fpp-link-bottom']")
# proceed_to_create_account_button
driver.find_element(By.XPATH, "//span[@id='intention-submit-button']//input[@type='submit']").click()

