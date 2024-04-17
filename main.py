from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера


options = webdriver.FirefoxOptions()
#options.add_argument("-P for_selenium")
options.binary_location = "/usr/bin/firefox"  # Укажите здесь правильный путь
service = Service(GeckoDriverManager().install())
browser = webdriver.Firefox(service=service, options=options)

browser.get("https://stepik.org/lesson/25969/step/8")
browser.quit()