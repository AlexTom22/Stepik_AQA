import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestLes(unittest.TestCase):
    def test_les16_step11_1(self):
        # try:
        link_web = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link_web)

        # Ваш код, который заполняет обязательные поля
        # browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "input.first").send_keys("Ivan")

        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Petrov")

        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")\
            .send_keys("i_petrov@gmail.com")

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
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Test down")

    # finally:
        sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_les16_step11_2(self):
        # try:
        link_web = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link_web)

        # Ваш код, который заполняет обязательные поля
        # browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "input.first").send_keys("Ivan")

        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Petrov")

        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")\
            .send_keys("i_petrov@gmail.com")

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
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Test down")

    # finally:
        sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
