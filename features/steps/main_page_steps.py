from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@given('Open target home page')
def open_main(context):
    context.app.main_page.open_main()


