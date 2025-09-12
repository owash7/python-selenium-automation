from selenium.webdriver.common.by import By
from behave import given, when, then

# Variables
BENEFIT_CELLS = (By.CSS_SELECTOR, "[class='cell-item-content']")
HEADER_LINKS = (By.CSS_SELECTOR, '[data-test*="@web/GlobalHeader/UtilityHeader/"]')
TARGET_CIR = (By.ID, 'utilityNav-circle')

@then('Verify page has at least {expected_amount} benefits cells')
def verify_benefits_cells(context, expected_amount):
        expected_amount = int(expected_amount)
        cells = context.driver.find_elements(*BENEFIT_CELLS)
        print(f'Found {len(cells)} benefit cells on the page')
        assert len(cells) >= expected_amount, f'Expected at least {expected_amount} cells but got {len(cells)}'

@when('Click on "Target Circle" button')
def click_tar_cir_btn(context):
    context.driver.find_element(*TARGET_CIR).click()


@then('Verify header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    print(f'Links {links}')
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'