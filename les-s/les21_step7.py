from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calc(z: str):
    return str(math.log(abs(12 * math.sin(int(z)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

try:
    # Открыть страницу http://suninjuly.github.io/get_attribute.html.
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    img = browser.find_element(By.ID, "treasure")

    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x: str = img.get_attribute("valuex")

    # Посчитать математическую функцию от x (сама функция остаётся неизменной).
    answer: str = calc(x)

    # Ввести ответ в текстовое поле.
    browser.find_element(By.ID, "answer").send_keys(answer)

    # Отметить checkbox "I'm the robot".
    browser.find_element(By.ID, "robotCheckbox").click()

    # Выбрать radiobutton "Robots rule!".
    browser.find_element(By.ID, "robotsRule").click()

    # Нажать на кнопку "Submit".
    browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
