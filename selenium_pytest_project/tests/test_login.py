import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.constants import BASE_URL, VALID_USER, VALID_PW


def test_successful_login(driver):
    # Start auf der Homepage
    driver.get(BASE_URL)
    home_page = HomePage(driver)

    # Navigation zum Login
    home_page.go_to_login()

    # Login durchführen
    login_page = LoginPage(driver)
    login_page.login(VALID_USER, VALID_PW)

    # Auf Account Button klicken
    home_page.click_account_button()

    # Verifikation ob Log-Out Button sichtbar ist
    logout_button = login_page.find(login_page.LOGOUT_BUTTON)
    assert logout_button.text == "Logout"