from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Variables
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton' or @data-test='@web/SearchButton']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div[data-test='shippingButton'][id*='addToCartButton']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test*='cartItem-title']")
CART_SUMMARY = (By.CSS_SELECTOR, "[data-test='cart-order-summary']")
CART_TOTAL = (By.CSS_SELECTOR, "[data-test='cart-summary-total']")


# Given go to target home page

# from target home page search for a product
@when('I search for {product_name}')
def search_product(context, product_name):
    search = context.driver.find_element(*SEARCH_FIELD)
    search.clear()
    search.send_keys(product_name)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(5)


# add product to cart
@when('Click on Add to Cart button')
def click_add_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(5)


# wait for side nav to show and add to cart
@when('Click Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(5)


@then('Open the cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')
    sleep(3)


@then('Verify cart has {product}')
def verify_product_name(context,product):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    expected_product_name = "toothpaste"
    assert expected_product_name in actual_name.lower(), f'Expected {expected_product_name} but got {actual_name}'


@then('Verify my cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart_summary, f'Expected {amount} items but got {cart_summary}'
