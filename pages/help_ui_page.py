from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class HelpUIPage(Page):
    HELP_CENTER_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-helpCenter']")
    HELP_ICON = (By.XPATH, "//h1[text()='Help']")
    HELP_SEARCH = (By.CSS_SELECTOR, "[id='helpSearch']")
    SEARCH_TOPIC = (By.CSS_SELECTOR, "h2[class*='styles']:nth-of-type(2)")
    SEARCH_BTN = (By.XPATH, "//button[normalize-space()='Search']")
    HELP_TILES = (By.CSS_SELECTOR, "div[class*='sc-a'] a")
    FIRST_TILE = (By.CSS_SELECTOR, "a[data-test='Track my order']")
    SELECT_TOPIC_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")
    HEADER = (By.XPATH, "//h1[text()= ' {SUBSTR}']")

    def click_help_center_btn(self):
        self.find_element(*self.HELP_CENTER_BTN)

    def verify_help_url(self):
        self.wait_until_urls_contains("https://www.target.com")

    def verify_help_tiles(self, count):
        self.wait_for_presence(*self.FIRST_TILE)
        self.verify_element_count(count, *self.HELP_TILES)

    def open_help_returns(self):
        self.open_url(f"https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges")

    def select_help_topic(self,help_topic):
        dd = self.find_element(*self.SELECT_TOPIC_DD)
        select = Select(dd)
        select.select_by_value(help_topic)


# Dynamic locator
    def get_locator(self, expected_header_text):
        # return [By..., "value"]
        return [self.HEADER[0], self.HEADER[1].replace("{SUBSTR}", expected_header_text)]

    def verify_header(self, expected_header_text):
        locator = self.get_locator(expected_header_text)
        self.wait_for_element_visible(*locator)