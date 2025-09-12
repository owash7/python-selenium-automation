from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

# Variables
ACCT_BTN = (By.ID, 'account-sign-in')
SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
SIGN_IN_TXT = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")


@when('Click the account button sign in button opens')
def click_account_button(context):
    context.driver.find_element(*ACCT_BTN).click()
    sleep(4)

@then('Click sign in button')
def click_sign_in_button(context):
    context.driver.find_element(*SIGN_IN_BTN).click()


@then("Verify 'Sign in or create account' text")
def verify_sign_in_msg(context):
    expected_text = 'Sign in or create account'
    actual_text = context.driver.find_element(*SIGN_IN_TXT).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'