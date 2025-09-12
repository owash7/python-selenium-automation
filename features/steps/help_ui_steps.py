from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

driver = webdriver.Chrome()

HELP_CENTER_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-helpCenter']")
HELP_ICON = (By.XPATH, "//h1[text()='Help']")
HELP_SEARCH = (By.CSS_SELECTOR, "[id='helpSearch']")


@then("Click the help center button")
def click_help_center_button(context):
    context.driver.find_element(*HELP_CENTER_BTN).click()
    sleep(7)


@then("Verify Help icon is present")
def help_center_icon_is_present(context):
    expected_text = "Help"
    actual_text = context.driver.find_element(*HELP_ICON).text
    assert expected_text == actual_text, f"Expected:{expected_text}, but got {actual_text}"

@then("Check if you can search for {topics}")
def check_for_topics(context, topics):
    search = context.driver.find_element(*HELP_SEARCH)
    search.click()
    search.send_keys(topics)
    sleep(2)
    search.click("ENTER")
    expected_result = f"{topics}"
    actual_result = context.driver.find_element((By.XPATH, f"//h2[contains(text(), '{topics}')]")).text
    assert expected_result in actual_result, f"Expected:{expected_result}, but got {actual_result}"
    driver.back()

