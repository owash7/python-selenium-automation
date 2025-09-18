from pages.base_page import Page
from pages.cart_page_page import Cart
from pages.header_page import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = Cart(driver)
        self.sign_in_page = SignInPage(driver)


