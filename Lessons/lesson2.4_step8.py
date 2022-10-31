import time
import math

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.common.by import By

# # For Firefox, Selenium 4
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def calc(z: str):
    return str(math.log(abs(12 * math.sin(int(z)))))

# For Chrome
# browser = webdriver.Chrome()


browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser.implicitly_wait(5)

try:

    # Открыть страницу
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    button = WebDriverWait(browser, 20).until(
        es.text_to_be_present_in_element((By.CSS_SELECTOR, ".card>.card-body #price"), "$100")
    )

    # Нажать на кнопку "Book"
    browser.find_element(By.CSS_SELECTOR, ".card>.card-body>#book").click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    # Пройти капчу для робота и получить число-ответ
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    answer = calc(x)
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn').click()

    print(browser.switch_to.alert.text)

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
