from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link_web = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()

try:

    browser.get(link_web)

    elements = browser.find_elements(By.CSS_SELECTOR, "form>div>input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "form>button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
