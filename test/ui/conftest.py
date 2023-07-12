import pytest
import time
import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# CHROME_WINDOW_SIZES = "--window-size=1280,720"
CHROME_WINDOW_SIZES = "--window-size=1920,1080"

# BROWSER_HEADLESS = True  # not visible
BROWSER_HEADLESS = False  # visible


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument(CHROME_WINDOW_SIZES)
    options.headless = BROWSER_HEADLESS
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    # driver.set_window_size(1920, 1080)
    # driver.set_window_size(1280, 720)
    # driver.maximize_window()
    browser.implicitly_wait(10)
    print("\nStart browser for test..       (from tests/ui/conftest.py file)")

    yield browser

    # следующий код выполнится после завершения теста
    print("\nQuit browser..                 (from tests/ui/conftest.py file)")
    browser.quit()



