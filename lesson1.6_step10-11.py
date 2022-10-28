from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


link_web = "http://suninjuly.github.io/registration1.html"
# link_web = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try:
    browser.get(link_web)

    # Ваш код, который заполняет обязательные поля
    # browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input.first").send_keys("Ivan")

    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Petrov")

    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("i_petrov@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "form>button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
