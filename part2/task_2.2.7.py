import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome"  # Укажите здесь правильный путь
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


link = "http://suninjuly.github.io/file_input.html"


try:
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder~=\"first\"]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder~=\"last\"]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder~=\"email\"]")
    input3.send_keys("Petrov@asdasd.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")

    button.click()
    time.sleep(5)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
