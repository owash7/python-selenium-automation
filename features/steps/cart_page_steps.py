from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Variables
CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test*='cartItem-title']")
CART_SUMMARY = (By.CSS_SELECTOR, "[data-test='cart-order-summary']")
HEADER = (By.CSS_SELECTOR, "[id='@web/component-header']")


@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart_msg(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


@then('Open the cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')
    context.wait.until(EC.visibility_of_element_located(HEADER))


@then('Verify cart has {product}')
def verify_product_name(context,product):
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text

    assert context.cart_item_title[:20] == product_name_in_cart[:20], \
        f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'


@then('Verify my cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f'Expected {amount} items but got {cart_summary}'