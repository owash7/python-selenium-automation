from pages.base_page import Page
from selenium.webdriver.common.by import By

class Cart(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    HEADER = (By.CSS_SELECTOR, "[id='@web/component-header']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test*='cartItem-title']")
    CART_SUMMARY = (By.CSS_SELECTOR, "[data-test='cart-order-summary']")


    def verify_cart_empty(self):
        self.wait_for_element_visible(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)


    def open_cart(self):
        self.open_url("https://www.target.com/cart")
        self.wait_for_presence(*self.HEADER)


    def verify_cart_has_products(self, product):
        self.wait_for_element_visible(*self.PRODUCT_TITLE)
        product = self.verify_partial_text(*self.PRODUCT_TITLE)
        return product


    def verify_cart_product_amount(self, amount):
        cart_summary = self.find_element(*self.CART_SUMMARY).text
        assert f'{amount} item' in cart_summary, f'Expected {amount} items but got {cart_summary}'