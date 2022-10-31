import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(z: str):
    return str(math.log(abs(12 * math.sin(int(z)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:

    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    browser.get(link)
    # Нажать на кнопку
    browser.find_element(By.CSS_SELECTOR, "button.trollface.btn").click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Пройти капчу для робота и получить число-ответ
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    answer = calc(x)
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"].btn').click()

    print(browser.switch_to.alert.text)

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
