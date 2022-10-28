from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

link_web = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()

try:

    browser.get(link_web)

    code = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(By.LINK_TEXT, code)
    link.click()

# фрагмент кода заполнения страницы авторизации
    input1 = browser.find_element(By.CSS_SELECTOR, "div > label + input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
