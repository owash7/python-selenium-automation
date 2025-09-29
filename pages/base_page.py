from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

# common commands
    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

# Action Chains
    def hover_over_element(self, *locator):
        element = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()


# Wait commands
    def wait_for_element_clickable_click(self, *locator, message=None):
         self.wait.until(EC.element_to_be_clickable(locator), message= f'Element by {locator} not clickable').click()

    def wait_for_element_visible(self, *locator, message=None):
        return self.wait.until(EC.visibility_of_element_located(locator), f'Element by {locator} did not appear')

    def wait_for_presence(self, *locator, message=None):
        return self.wait.until(EC.presence_of_element_located(locator),f'Element by {locator} not located')

    def wait_for_element_invisible(self, *locator, message=None):
        self.wait.until(EC.invisibility_of_element(locator), f'Element by {locator} not invisible')

    def wait_until_urls_contains(self, partial_url, message=None):
        self.wait.until(EC.url_contains(partial_url),
            message=f'Current url does not contain {partial_url}')


    def get_current_url(self):
        return self.driver.current_url


# Verification Commands
    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f'Expected {expected_url}, but got {actual_url}'


    def verify_partial_url(self, expected_partial_url):
        actual_partial_url = self.driver.current_url
        assert expected_partial_url in actual_partial_url, f'Expected {expected_partial_url}, but got {actual_partial_url}'


    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text}, but got {actual_text}'


    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_partial_text in actual_text, f'Expected {expected_partial_text}, but got {actual_text}'

    def verify_element_count(self, expected_count, *locator):
        expected_count = int(expected_count)
        elements = self.find_elements(*locator)
        actual_count = len(elements)
        assert actual_count == expected_count, f'Expected {expected_count}, but got {actual_count}'

