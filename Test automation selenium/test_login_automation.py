import pytest
from selenium import webdriver
from login_automation import login_automation
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize("user", [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
])
def test_all_user_login(driver, user):
    # Pytest ruft für jeden 'user' die Funktion auf
    login_automation(driver, user, "secret_sauce")

    # Ergebnis prüfen
    item = driver.find_element(By.CLASS_NAME, "title")
    assert item.text == "Products"


def test_item(driver):
    # User Login
    login_automation(driver, "standard_user", "secret_sauce")

    # Ergebnis prüfen
    item = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")
    assert item.text == "Sauce Labs Backpack"



