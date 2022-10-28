import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(z: str):
    return str(math.log(abs(12 * math.sin(int(z)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:

    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser.get(link)

    # Нажать на кнопку
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Принять confirm
    confirm = browser.switch_to.alert.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    # browser.implicitly_wait(5)
    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)
    browser.find_element(By.ID, "answer").send_keys(answer)

    butt = browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"].btn')
    butt.click()

    print(browser.switch_to.alert.text)

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
