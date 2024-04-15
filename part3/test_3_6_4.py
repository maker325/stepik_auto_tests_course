
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_authorization(browser, load_config):
    link = f"https://stepik.org/lesson/236895/step/1"
    login = load_config['login_stepik']
    password = load_config['password_stepik']
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, "#ember420")
    button1.click()
    input1 = browser.find_element(By.NAME, "login")
    input1.send_keys(login)
    input2 = browser.find_element(By.NAME, "password")
    input2.send_keys(password)
    button2 = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    button2.click()
    boolean = WebDriverWait(browser, 5).until(
        ec.text_to_be_present_in_element((By.TAG_NAME, "p"), "test input")
    )
    assert boolean
