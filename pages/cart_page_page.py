from pages.base_page import Page
from selenium.webdriver.common.by import By

class Cart(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    HEADER = (By.CSS_SELECTOR, "[id='@web/component-header']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test*='cartItem-title']")
    CART_SUMMARY = (By.CSS_SELECTOR, "[data-test='cart-order-summary']")


    def verify_cart_empty(self):
        expected_text = 'Your cart is empty'
        self.wait_for_element_visible(*self.CART_EMPTY_MSG)
        actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


    def open_cart(self):
        self.open_url("https://www.target.com/cart")
        self.wait_for_presence(*self.HEADER)


    def verify_cart_has_products(self, product):
        product_name_in_cart = self.find_element(*self.PRODUCT_TITLE).text
        assert product[:20] == product_name_in_cart[:20], \
            f'Expected {product[:20]} did not match {product_name_in_cart[:20]}'


    def verify_cart_product_amount(self, amount):
        cart_summary = self.find_element(*self.CART_SUMMARY).text
        assert f'{amount} item' in cart_summary, f'Expected {amount} items but got {cart_summary}'