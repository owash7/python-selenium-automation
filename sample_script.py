from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# create a new Chrome browser instance
driver = webdriver.Chrome()
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)


# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('table')


search_btn = (By.NAME, 'btnK')
# click search button
search = driver.wait.until(EC.element_to_be_clickable(search_btn))
search.click()

# verify search results
assert 'table'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
