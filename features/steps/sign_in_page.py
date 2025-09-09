from selenium.webdriver.common.by import By
from behave import given, when, then

acct_btn = (By.ID, 'account-sign-in')
sign_in_btn = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
sign_in_txt = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")


@when('Click the account button sign in button opens')
def click_account_button(context):
    context.driver.find_element(*acct_btn).click()


@then('Click sign in button')
def click_sign_in_button(context):
    context.driver.find_element(*sign_in_btn).click()


@then("Verify 'Sign in or create account' text")
def verify_sign_in_msg(context):
    expected_text = 'Sign in or create account'
    actual_text = context.driver.find_element(*sign_in_txt).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'