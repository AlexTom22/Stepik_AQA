import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calc(z: str):
    return str(math.log(abs(12 * math.sin(int(z)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:

    # Открыть страницу
    browser.get(link)

    # Считать значение для переменной x.
    x = browser.find_element(By.ID, "input_value").text

    # Посчитать математическую функцию от x.
    answer = calc(x)

    # Проскроллить страницу вниз.
    button = browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Ввести ответ в текстовое поле.
    text_box_answer = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_box_answer)
    text_box_answer.send_keys(answer)

    # Выбрать checkbox "I'm the robot".
    browser.find_element(By.ID, "robotCheckbox").click()

    # Переключить radiobutton "Robots rule!".
    browser.find_element(By.ID, "robotsRule").click()

    # Нажать на кнопку "Submit".
    browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
