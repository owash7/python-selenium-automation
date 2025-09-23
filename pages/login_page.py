from pages.base_page import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):
    PP_LINK = (By.CSS_SELECTOR, "[aria-label*='privacy policy']")

    def open_target_login(self):
        self.open_url("https://www.target.com/orders?lnk=acct_nav_my_account")

    def click_privacy_policy_link(self):
        self.click(*self.PP_LINK)
