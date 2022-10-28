from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calc(z: str):
    return str(math.log(abs(12 * math.sin(int(z)))))


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    # Открыть страницу
    browser.get(link)

    # по #num1 получить первое число
    num1 = browser.find_element(By.ID, "num1").text

    # по #num2 получить второе число
    num2 = browser.find_element(By.ID, "num2").text

    # сложить их в summa
    summa: str = str(int(num1) + int(num2))

    # найти выпадающий список по select#dropdown
    browser.find_element(By.CSS_SELECTOR, 'select#dropdown').click()

    # выбрать value равное сумме
    css_str = "[value = '" + summa + "']"
    browser.find_element(By.CSS_SELECTOR, css_str).click()

    # нажать кнопку submit
    browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
