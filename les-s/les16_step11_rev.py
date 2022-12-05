from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element(By.XPATH, "//input[@class='form-control first'][@required]")
    input_first_name.send_keys("Ivan")

    css_loc = ".first_block > .second_class > input"
    browser.find_element(By.CSS_SELECTOR, css_loc).send_keys("Petrov")

    css_loc = ".first_block > .third_class > input"
    input_email = browser.find_element(By.CSS_SELECTOR, css_loc)
    input_email.send_keys("i_petrov@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
