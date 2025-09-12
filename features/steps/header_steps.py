from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Variables
CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


