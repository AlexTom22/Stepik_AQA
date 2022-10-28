from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calc(z: str):
    return str(math.log(abs(12 * math.sin(int(z)))))


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    # Открыть страницу https://suninjuly.github.io/math.html.
    browser.get(link)

    # Считать значение для переменной x.
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x: str = x_element.text

    # Посчитать математическую функцию от x.
    y: str = calc(x)

    # Ввести ответ в текстовое поле.
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # Отметить checkbox "I'm the robot".
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбрать radiobutton "Robots rule!".
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
