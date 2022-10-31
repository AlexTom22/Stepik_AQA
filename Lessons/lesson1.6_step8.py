from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


link_web = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()

try:

    browser.get(link_web)

    input1 = browser.find_element(By.XPATH, "//form/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//form/div[2]/input')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//form/div[3]/input')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.XPATH, '//form/div[4]/input')
    input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, "//div/button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
