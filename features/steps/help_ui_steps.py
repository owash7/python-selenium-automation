from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then


HELP_CENTER_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-helpCenter']")
HELP_ICON = (By.XPATH, "//h1[text()='Help']")
HELP_SEARCH = (By.CSS_SELECTOR, "[id='helpSearch']")


@then("Click the help center button")
def click_help_center_btn(context):
    context.app.help_ui_page.click_help_center_btn()


@then("Verify Help page url")
def verify_help_url(context):
    context.app.help_ui_page.verify_help_url()

@then("Verify {count} help tiles are on page")
def verify_help_tiles(context, count):
    context.app.help_ui_page.verify_help_tiles(count)
