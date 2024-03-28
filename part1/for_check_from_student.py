import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# failing test
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome"  # Укажите здесь правильный путь

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get(link)

first_name_field = browser.find_element(by=By.CSS_SELECTOR, value='input[placeholder="Input your first name"]')
first_name_field.send_keys("Kate")

last_name_field = browser.find_element(by=By.CSS_SELECTOR, value='input[placeholder="Input your last name"]')
last_name_field.send_keys("Bibilova")

email_field = browser.find_element(by=By.CSS_SELECTOR, value='input[placeholder="Input your email"]')
email_field.send_keys("kate@gmail.com")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.TAG_NAME, "h1"))
)

welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text

browser.quit()
