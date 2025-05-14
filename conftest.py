import pytest
from selene import browser


@pytest.fixture(autouse=True)
def test_open_browser():
    browser.open("https://duckduckgo.com/")

def browser_size():
    browser.config.window_width = 600
    browser.config.window_height = 800 #как в старые добрые времена
    yield
    browser.quit()