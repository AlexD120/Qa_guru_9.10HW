from selene import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1280
    browser.config.window_height = 1024

    yield

    browser.quit()