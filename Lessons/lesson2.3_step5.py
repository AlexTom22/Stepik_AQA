import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


try:

# # Variant 1
    with webdriver.Chrome() as browser:
        result = []
        browser.get('http://parsinger.ru/blank/2/1.html')
        time.sleep(1)
        browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
        browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
        browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')

        time.sleep(1)
        for x in reversed(range(len(browser.window_handles))):
            browser.switch_to.window(browser.window_handles[x])
            for y in browser.find_elements(By.CLASS_NAME, 'check'):
                y.click()

# # Variant 2
#     result = []
#     with webdriver.Chrome() as browser:
#         for x in range(1, 7):
#             blank = browser.execute_script(f'window.open("http://parsinger.ru/blank/1/{x}.html", "_blank{x}");')
#         tabs = browser.window_handles
#         for z in range(len(tabs) - 1):
#             if not browser.execute_script("return document.title;"):
#                 browser.close()
#             time.sleep(1)
#             browser.switch_to.window(browser.window_handles[z])
#             browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
#             result.append(int(browser.find_element(By.ID, 'result').text))
#             print(browser.find_element(By.ID, 'result').text)
#     print(result)


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
