from behave import given, when, then


@given("Open help page for Returns")
def open_help_returns(context):
    context.app.help_ui_page.open_help_returns()


@then("Click the help center button")
def click_help_center_btn(context):
    context.app.help_ui_page.click_help_center_btn()


@then("Verify Help page url")
def verify_help_url(context):
    context.app.help_ui_page.verify_help_url()


@then("Verify {count} help tiles are on page")
def verify_help_tiles(context, count):
    context.app.help_ui_page.verify_help_tiles(count)


@when("Select Help topic {help_topic}")
def select_help_topic(context, help_topic):
    context.app.help_ui_page.select_help_topic(help_topic)

@then("Verify help {expected_header_text} page opened")
def verify_help_topic_opened(context, expected_header_text):
    context.app.help_ui_page.verify_header(expected_header_text)


