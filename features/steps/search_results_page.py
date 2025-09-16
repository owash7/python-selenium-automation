from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep



SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div[data-test='shippingButton'][id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


# add product to cart
@when('Click on Add to Cart button')
def click_add_cart(context):
    add_cart = context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN),
    message='The product name was not found.')
    add_cart.click()


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored: ', context.product_name)
    context.wait.until(EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME))


# wait for side nav to show and add to cart
@when('Click Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    side_nav_add_btn = context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN)
    side_nav_add_btn.click()
    context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN),
    message='Side navigation add to cart btn was not clickable.')


@then('Verify search results are shown for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TXT).text
    assert product in actual_text, f'Error. Expected text {product} but got {actual_text}'