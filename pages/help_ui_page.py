from pages.base_page import Page
from selenium.webdriver.common.by import By


class HelpUIPage(Page):
    HELP_CENTER_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-helpCenter']")
    HELP_ICON = (By.XPATH, "//h1[text()='Help']")
    HELP_SEARCH = (By.CSS_SELECTOR, "[id='helpSearch']")
    SEARCH_TOPIC = (By.CSS_SELECTOR, "h2[class*='styles']:nth-of-type(2)")
    SEARCH_BTN = (By.XPATH, "//button[normalize-space()='Search']")
    HELP_TILES = (By.CSS_SELECTOR, "div[class*='sc-a'] a")
    FIRST_TILE = (By.CSS_SELECTOR, "a[data-test='Track my order']")

    def click_help_center_btn(self):
        self.find_element(*self.HELP_CENTER_BTN)


    def verify_help_url(self):
        self.wait_until_urls_contains("https://www.target.com")

    def verify_help_tiles(self, count):
        self.wait_for_presence(*self.FIRST_TILE)
        self.verify_element_count(count, *self.HELP_TILES)
