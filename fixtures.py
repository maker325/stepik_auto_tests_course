import pytest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



@pytest.fixture(autouse=True) # Пока не обращаем внимания на эту строку
def get_driver(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"  # Укажите здесь правильный путь
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
