from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math
import pytest


@pytest.mark.parametrize('link_code', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_authorization(browser, load_config, link_code):
    link = f"https://stepik.org/lesson/236{link_code}/step/1"
    login = load_config['login_stepik']
    password = load_config['password_stepik']
    browser.get(link)
    button1 = browser.find_element(By.XPATH, "//a[text()=\"Войти\"]")
    button1.click()
    input1 = browser.find_element(By.NAME, "login")
    input1.send_keys(login)
    input2 = browser.find_element(By.NAME, "password")
    input2.send_keys(password)
    button2 = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    button2.click()
    time.sleep(5)
    input3 = browser.find_element(By.CSS_SELECTOR, "textarea")
    answer = str(math.log(int(time.time())))
    input3.send_keys(answer)
    button3 = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    button3.click()
    element = WebDriverWait(browser, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
    )
    result = element.text
    if result != "Correct!":
        print(result)
