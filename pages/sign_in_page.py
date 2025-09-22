from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    SIGN_IN_TXT = (By.XPATH, "//h1[text()='Sign in or create account']")
    USERNAME_FIELD = (By.ID, "username")
    SIGN_IN_CON = (By.ID, "login")
    PW_BTN = (By.ID, "password")
    SIGN_IN_W_PW = (By.XPATH, "//button[text()='Sign in with password']")
    ACCT_SIGN_IN = (By.ID, "account-sign-in")

    def click_sign_in_btn(self):
        self.wait_for_element_clickable_click(*self.SIGN_IN_BTN)


    def verify_sign_in_button_text(self):
        self.wait_for_element_visible(*self.SIGN_IN_TXT)
        self.verify_text('Sign in or create account', *self.SIGN_IN_TXT)


    def sign_in_user(self,email):
        self.wait_for_element_clickable_click(*self.USERNAME_FIELD)
        self.input_text(email,*self.USERNAME_FIELD)
        self.click(*self.SIGN_IN_CON)


    def click_sign_in_by_password(self):
        self.click(*self.PW_BTN)

    def enter_password(self,password):
        self.wait_for_element_clickable_click(*self.PW_BTN)
        self.input_text(password,*self.PW_BTN)
        self.click(*self.SIGN_IN_W_PW)


    def verify_user_is_signed_in(self,user):
        self.wait_for_element_visible(*self.ACCT_SIGN_IN)
        self.verify_partial_text(user, *self.ACCT_SIGN_IN)



