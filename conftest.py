import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_setup():
    browser.config.base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    browser.config.window_width = 1080
    browser.config.window_height = 1920
    yield
    browser.quit()
