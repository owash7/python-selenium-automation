from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
VARIANT = (By.CSS_SELECTOR, '[data-test="@web/VariationComponent"]')

@given('Open target product A-91269718 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718?preselect=90919011#lnk=sametab')
    context.wait.until(EC.presence_of_element_located(VARIANT), message='No options available')


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Navy Denim', 'Dark Wash', 'Light Wash']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for color in colors:
        color.click()
        # for visibility only:
        sleep(0.5)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'