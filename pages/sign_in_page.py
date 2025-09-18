from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    SIGN_IN_TXT = (By.XPATH, "//h1[text()='Sign in or create account']")


    def click_sign_in_btn(self):
        self.wait_for_element_clickable(*self.SIGN_IN_BTN)
        self.click(*self.SIGN_IN_BTN)


    def verify_sign_in_button_text(self):
        expected_text = 'Sign in or create account'
        self.wait_for_element_visible(*self.SIGN_IN_TXT)
        actual_text = self.find_element(*self.SIGN_IN_TXT).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
