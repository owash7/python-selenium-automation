from selenium.webdriver.common.by import By
from behave import given, when, then


LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_IMG = (By.CSS_SELECTOR, "img")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")


# add product to cart
@when("Click on product")
def click_product(context):
    context.app.search_results_page.click_product()


# @when('Store product name')
# def store_product_name(context):
#     context.app.search_results_page.click_product()


@when("Click add to cart button")
def add_to_cart_btn(context):
    context.app.search_results_page.add_to_cart_btn()

# wait for side nav to show and add to cart
@when("Click Add to Cart button from side navigation")
def side_nav_click_add_to_cart(context):
    context.app.search_results_page.add_button_side_nav()


@when("Hover favorites icon")
def hover_fav_icon(context):
    context.app.search_results_page.hover_fav_icon()


@then("Favorites tooltip is shown")
def verify_fav_tt_shown(context):
    context.app.search_results_page.verify_fav_tt_shown()


@then("Verify search results are shown for {product}")
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)


@then("Verify that every product has a name and image")
def verify_product_name_and_image(context):
    # context.driver.execute_script("window.scrollBy(0,2000", "")
    # context.driver.execute_script("window.scrollBy(0,1000", "")

    products = context.driver.find_elements(*LISTINGS)

    for product in products[:8]:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Error. Product title was not found.'
        img = product.find_element(*PRODUCT_IMG)
        assert img, 'Error. Product image was not found.'

