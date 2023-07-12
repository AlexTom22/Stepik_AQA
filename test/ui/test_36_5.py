import pytest
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_BUT_CSS = "#ember33"
LOGIN_CSS = "input[name='login']"
PASS_CSS = "input[name='password']"
SUBMIT_CSS = "button[type='submit']"
my_login = "qa.tomelo.an@gmail.com"
my_password = "ATom-1967"
ANSWER_LOC = (By.CSS_SELECTOR, "#ember91")
ANSWER_FILD = "#ember91"
BUTTON_SEND = "button.submit-submission"
CORRECT_LOC = "#ember96"


@pytest.mark.parametrize(
    "url",
    [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
    ]
)
def test_login(browser, url):
    browser.delete_all_cookies()
    browser.get(url)
    browser.find_elements(By.CSS_SELECTOR, LOGIN_BUT_CSS)
    browser.find_element(By.CSS_SELECTOR, LOGIN_BUT_CSS).click()
    browser.find_element(By.CSS_SELECTOR, LOGIN_CSS).send_keys(my_login)
    browser.find_element(By.CSS_SELECTOR, PASS_CSS).send_keys(my_password)
    browser.find_element(By.CSS_SELECTOR, SUBMIT_CSS).click()
    Wait(browser, 5).until(
        EC.visibility_of_element_located(ANSWER_LOC)
    )

    text_fild = browser.find_element(*ANSWER_LOC)
    ans = answer()
    text_fild.send_keys(ans)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, BUTTON_SEND).click()
    time.sleep(2)

    line = browser.find_elements(By.CSS_SELECTOR, CORRECT_LOC)
    if line.text() != "Correct!":
        pytest.fail(line.text())


# @pytest.fixture()
def answer():
    return str(math.log(int(time.time())))
