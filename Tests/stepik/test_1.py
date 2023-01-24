from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    time.sleep(1)

    button = browser.find_element(By.ID, "submit_button")
    time.sleep(1)

    button.click()
    time.sleep(1)

# закрываем браузер после всех манипуляций
finally:
    browser.quit()
