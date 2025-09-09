from selenium import webdriver
from selenium.webdriver.common.by import By


# Start Chrome browser:
driver = webdriver.Chrome()

driver.get('https://stackoverflow.com/users/signup')

# XPATH for create account
driver.find_element(By.XPATH, "//h1[text()='Create your account']")

# CSS selector for terms of conditions
driver.find_element(By.CSS_SELECTOR, "[name='tos']")

# CSS selector for privacy policy
driver.find_element(By.CSS_SELECTOR, "[name='privacy']")

# Email locator with ID
driver.find_element(By.ID, 'email')

# Password locator with ID
driver.find_element(By.ID, 'password')

# Show password icon with CSS
driver.find_element(By.CSS_SELECTOR, "[class*='js-show-password']")

# Sign in button with ID
driver.find_element(By.ID, 'submit-button')

# Sign up with google CSS
driver.find_element(By.CSS_SELECTOR, "[data-provider='google']")

# Sign up with github CSS
driver.find_element(By.CSS_SELECTOR, "[data-provider='github']")
