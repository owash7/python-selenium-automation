from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.options import Options


def browser_init(context):
#def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome()

    ## BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # options = webdriver.ChromeOptions()
    # bstack_options = {
    #     "os": "Windows",
    #     "osVersion": "10",
    #     'browserName': 'Edge',
    #     'sessionName': scenario_name,
    #     "buildName": "Selenium Test Run",
    #     "projectName": "My Test Project",
    #     "debug": True,
    #     "networkLogs": True,
    #     "consoleLogs": "info",
    #     'userName': 'oshawashington_goDHf3',
    #     'accessKey': 'bssjk1Wx5dh5cxeVsFxA'
    # }
    #
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(
    #     command_executor='https://hub-cloud.browserstack.com/wd/hub',
    #     options=options
    # )

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context,scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
