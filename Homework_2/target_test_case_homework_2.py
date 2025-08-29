from selenium import webdriver
from selenium.webdriver import Keys
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

# Open Target home page
url = "https://www.target.com/"
driver.get(url)
sleep(4)

# Click on Account button
driver.find_element(By.ID, 'account-sign-in').click()
sleep(4)

# Click on sign in or create account button from side navigation
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(3)

# Verify “Sign in or create account” text is shown
actual_text = driver.find_element(By.XPATH, "//h1[normalize-space()='Sign in or create account']").text
expected_text = 'Sign in or create account'
assert expected_text in actual_text
print("Success!")

# Extra seps needed to get to sign in button
driver.find_element(By.ID, 'username').send_keys('washingtonosha209@yahoo.com')
driver.find_element(By.ID, 'username').send_keys(Keys.ENTER)
sleep(4)
driver.find_element(By.ID, 'password').click()
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in with password']")
sleep(4)

driver.quit()

