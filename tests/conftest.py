from selenium import webdriver
from settings import config
import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():

    browser.config.base_url = config.base_url
    browser.config.driver_name = config.driver_name
    browser.config.timeout = config.timeout

    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.headless = config.headless

    if config.headless:
        driver_options = webdriver.ChromeOptions() if config.driver_name == 'chrome' \
            else webdriver.FirefoxOptions()
        driver_options.add_argument('--headless=new')
        browser.config.driver_options = driver_options

