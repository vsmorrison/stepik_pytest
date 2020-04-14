import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language', 
        action='store', 
        default="ru-Ru",
        help="Choose language: en/es/fr/ru"
        )


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    browser_language = request.config.getoption("language")
    options.add_experimental_option(
        'prefs', 
        {'intl.accept_languages': browser_language}
        )
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
