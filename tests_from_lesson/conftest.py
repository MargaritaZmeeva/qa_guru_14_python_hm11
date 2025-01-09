import pytest
from selene import browser

@pytest.fixture(autouse=True)
def browser_setup():
    browser.config.window_height = 720  # задает высоту окна браузера
    browser.config.window_width = 360  # задает ширину окна браузера
    browser.config.base_url = "https://google.com"
    yield
    browser.quit()


