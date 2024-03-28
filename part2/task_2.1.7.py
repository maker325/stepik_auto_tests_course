import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome"  # Укажите здесь правильный путь

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    browser.get(link)
    box = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = box.get_attribute("valuex")
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    # Отправляем заполненную форму
    time.sleep(3)
    button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла