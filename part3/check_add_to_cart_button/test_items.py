import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def test_presence_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    try:
        button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        time.sleep(5)
        assert button is not None, "Button not found"
    except NoSuchElementException:
        assert False, "Button not found"
