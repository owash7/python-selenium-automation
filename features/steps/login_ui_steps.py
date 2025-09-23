from behave import given,when,then

@given("Open target login page")
def open_target_login(context):
    context.app.login_page.open_target_login()

@given("Store original window")
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print("Original window is:", context.original_window)

@when("Click Privacy Policy link")
def click_privacy_link(context):
    context.app.login_page.click_privacy_policy_link()

@when("Switch to new window")
def switch_window(context):
    current_window = context.driver.window_handles
    new_window = current_window[1]
    context.driver.switch_to.window(new_window)

@then("Verify Privacy Policy page opened")
def verify_privacy_policy_opened(context):
    context.app.privacy_policy_page.verify_pp_opened()

@then("Close current window")
def close_current_window(context):
    context.driver.close()

@then("Return to original window")
def return_original_window(context):
    context.driver.switch_to.window(context.original_window)