import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test...    fixture from tests/test_fixture7.py file")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser...              fixture from tests/test_fixture7.py file")
#     browser.quit()


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
