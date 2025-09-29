from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR,
        "div[data-test='shippingButton'][id*='addToCartButton']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    PRODUCT_TOKEN = (By.CSS_SELECTOR, "a[data-test='product-title']")
    POP_UP_BANNER = (By.CSS_SELECTOR, "[class='heroImg']")
    FAV_ICON = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAV_TT_TEXT = (By.XPATH, "//*[contains(text(), 'Click to sign in and save')]")

    def verify_search_results(self, product):
        self.wait_for_element_visible(*self.SEARCH_RESULTS_TXT)
        self.verify_partial_text(product,*self.SEARCH_RESULTS_TXT)


    def click_product(self):
        sleep(4)
        self.wait_for_element_invisible(*self.POP_UP_BANNER)
        self.wait_for_element_clickable_click(*self.PRODUCT_TOKEN)


    def add_to_cart_btn(self):
        sleep(2)
        self.wait_for_element_clickable_click(*self.ADD_TO_CART_BTN)


    def store_product_name(self):
        self.wait_for_presence(*self.SIDE_NAV_PRODUCT_NAME)
        product_name = self.verify_text(*self.SIDE_NAV_PRODUCT_NAME)
        return product_name


    def add_button_side_nav(self):
        self.wait_for_element_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BTN)


    def verify_product_url(self, product):
        self.verify_partial_url(f'searchTerm={product}')


    def hover_fav_icon(self):
        self.hover_over_element(*self.FAV_ICON)

    def verify_fav_tt_shown(self):
        self.wait_for_element_visible(*self.FAV_TT_TEXT)

