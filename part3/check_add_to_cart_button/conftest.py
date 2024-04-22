import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="es",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    user_language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    executable_path = '/usr/bin/chromedriver'
    service = ChromeService(executable_path=executable_path)
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
