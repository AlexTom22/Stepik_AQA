import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..       (fixture from .conftest.py file)")
    browser = webdriver.Chrome()
    yield browser

    # следующий код выполнится после завершения теста
    print("\nquit browser..                 (fixture from .conftest.py file)")
    browser.quit()
