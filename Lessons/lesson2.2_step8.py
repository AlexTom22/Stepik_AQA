import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:

    # Открыть страницу http://suninjuly.github.io/file_input.html
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys("Alexander")
    browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]').send_keys("Tomelo")
    browser.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("aqa.tomelo.an@gmail.com")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "../file.txt")
    browser.find_element(By.ID, 'file').send_keys(file_path)

    # Нажать кнопку "Submit"
    browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
