from behave import given, when, then


@then('Click sign in button')
def click_sign_in_button(context):
    context.app.sign_in_page.click_sign_in_btn()


@then("Verify 'Sign in or create account' text")
def verify_sign_in_msg(context):
    context.app.sign_in_page.verify_sign_in_button_text()