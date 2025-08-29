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

# open the url
driver.get('https://www.target.com/')
# search field
driver.find_element(By.ID, 'search').send_keys('toilet paper')
# search button
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(7)

# Verify
actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
expected_text = 'toilet paper'.lower()
assert expected_text in actual_text, f"Expected: {expected_text}, Actual: {actual_text}"
print('Success!')
sleep(5)