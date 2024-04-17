import json
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"  # Укажите здесь правильный путь
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config

