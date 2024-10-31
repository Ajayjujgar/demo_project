import pytest
from selenium import webdriver


@pytest.fixture()
def startup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    return driver


@pytest.fixture(params=[
    ("standard_user", "secret_sauce", "Pass"),
    ("standard_userr", "secret_sauce", "Fail"),
    ("standard_user", "secret_saucee", "Fail"),
    ("standard_userr", "secret_saucee", "Fail")
])
def DataForLogin(request):
    return request.param
