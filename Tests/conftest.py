import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..       (from tests/conftest.py file)")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser

    # следующий код выполнится после завершения теста
    print("\nquit browser..                 (from tests/conftest.py file)")
    browser.quit()
