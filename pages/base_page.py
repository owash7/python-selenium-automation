from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)


    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        return self.driver.find_element(*locator)


    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_clickable(self, *locator, message=None):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_visible(self, *locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_presence(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

