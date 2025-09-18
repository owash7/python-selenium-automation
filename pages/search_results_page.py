from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR,
        "div[data-test='shippingButton'][id*='addToCartButton']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

    def verify_search_results(self, product):
        self.wait_for_element_visible(*self.SEARCH_RESULTS_TXT)
        actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text
        assert product in actual_text, f'Error. Expected text {product} but got {actual_text}'


    def click_add_to_cart(self):
        self.wait_for_element_clickable(*self.ADD_TO_CART_BTN,
                    message='Add To Cart Button not found for product')
        self.find_element(*self.ADD_TO_CART_BTN)


    def store_product_name(self):
        self.wait_for_presence(*self.SIDE_NAV_PRODUCT_NAME)
        product_name = self.find_element(*self.SIDE_NAV_PRODUCT_NAME).text
        print(f'Product name stored: {product_name}')
        return product_name



    def add_button_side_nav(self):
        self.wait_for_element_clickable(*self.SIDE_NAV_ADD_TO_CART_BTN,
                    message='Side navigation add to cart btn was not clickable.')
        self.click(*self.SIDE_NAV_ADD_TO_CART_BTN)


