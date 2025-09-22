from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton'"
                            " or @data-test='@web/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    TARGET_CIR = (By.ID, "utilityNav-circle")
    HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    BENEFIT_CELLS = (By.CSS_SELECTOR, "[class='cell-item-content']")
    ACCT_BTN = (By.ID, "account-sign-in")


    def search_product(self,product_name):
        self.input_text(product_name,*self.SEARCH_FIELD)
        self.wait_for_element_clickable_click(*self.SEARCH_BTN)


    def click_account_btn(self):
        self.click(*self.ACCT_BTN)


    def click_cart(self):
        self.click(*self.CART_ICON)


    def target_circle(self):
        self.click(*self.TARGET_CIR)


    def verify_header_link_count(self, expected_amount):
            self.verify_element_count(expected_amount, *self.HEADER_LINKS)


    def circle_benefits(self, expected_amount):
        expected_amount = int(expected_amount)
        cells = self.find_elements(*self.BENEFIT_CELLS)
        print(f'Found {len(cells)} benefit cells on the page')
        assert len(cells) >= expected_amount, f'Expected at least {expected_amount} cells but got {len(cells)}'

