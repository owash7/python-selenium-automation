from behave import given, when, then


@then("Click sign in button")
def click_sign_in_button(context):
    context.app.sign_in_page.click_sign_in_btn()


@then("Verify 'Sign in or create account' text")
def verify_sign_in_msg(context):
    context.app.sign_in_page.verify_sign_in_button_text()


@then("Enter user {email}")
def enter_user_email(context,email):
    context.app.sign_in_page.sign_in_user(email)

@then("Click sign in by password button")
def click_sign_in_by_password(context):
    context.app.sign_in_page.click_sign_in_by_password()

@then("Enter password {password}")
def enter_password(context,password):
    context.app.sign_in_page.enter_password(password)

@then("Verify {user} is signed in")
def verify_user_is_signed_in(context,user):
    context.app.sign_in_page.verify_user_is_signed_in(user)