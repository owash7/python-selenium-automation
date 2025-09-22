from pages.base_page import Page
from selenium.webdriver.common.by import By

class ProductDetailsPage(Page):
    VARIANT = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent']")

    def open_taget_details(self):
        self.open_url(f"https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718?preselect=90919011#lnk=sametab")
        self.wait_for_element_visible(*self.VARIANT, message="No options available")
