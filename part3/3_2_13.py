import unittest
import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome"  # Укажите здесь правильный путь
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)


link = "http://suninjuly.github.io/registration2.html"

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder~=\"first\"]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder~=\"last\"]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder~=\"email\"]")
        input3.send_keys("Petrov@asdasd.ru")
        # Отправляем заполненную форму
        time.sleep(2)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    def test_abs2(self):
        browser.get("http://suninjuly.github.io/registration2.html")

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder~=\"first\"]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder~=\"last\"]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder~=\"email\"]")
        input3.send_keys("Petrov@asdasd.ru")
        # Отправляем заполненную форму
        time.sleep(2)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)



    if __name__ == "__main__":
        unittest.main()

