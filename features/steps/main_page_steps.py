from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver


@given('Open target home page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    context.driver.maximize_window()
    sleep(4)