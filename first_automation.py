from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.amazon.com/"
driver.get(url)
search_field = driver.find_element(By.ID, "twotabsearchtextbox")
search_field.click()
search_field.send_keys("laptops")
sleep(3)

search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()
sleep(5)

driver.quit()


#driver.find_element(By.XPATH,'Best Sellers')
