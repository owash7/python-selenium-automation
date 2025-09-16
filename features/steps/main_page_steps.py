from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton' or @data-test='@web/SearchButton']")
HEADER = (By.CSS_SELECTOR, "[id='@web/component-header']")


@given('Open target home page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    context.driver.maximize_window()
    context.driver.wait.until(EC.visibility_of_element_located(HEADER))


# from target home page search for a product
@when('I search for {product_name}')
def search_product(context, product_name):
    search_field = context.driver.find_element(*SEARCH_FIELD)
    search_field.clear()
    search_field.send_keys(product_name)
    context.driver.find_element(*SEARCH_BTN).click()
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_FIELD))