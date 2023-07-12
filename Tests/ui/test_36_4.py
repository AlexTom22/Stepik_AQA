# import pytest
import time
from selenium.webdriver.common.by import By

LOGIN_BUT_CSS = "#ember33"
LOGIN_CSS = "input[name='login']"
PASS_CSS = "input[name='password']"
SUBMIT_CSS = "button[type='submit']"
my_login = "qa.tomelo.an@gmail.com"
my_password = "ATom-1967"


def test_login(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, LOGIN_BUT_CSS).click()
    browser.find_element(By.CSS_SELECTOR, LOGIN_CSS).send_keys(my_login)
    browser.find_element(By.CSS_SELECTOR, PASS_CSS).send_keys(my_password)
    browser.find_element(By.CSS_SELECTOR, SUBMIT_CSS).click()

    # дождаться того, что поп-апа с авторизацией больше нет
    act_url = "https://stepik.org/lesson/236895/step/1?auth=login"
    assert browser.current_url == act_url, "Авторизация не прошла"
    time.sleep(5)
