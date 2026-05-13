import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utils.constants import BASE_URL
from utils.helpers import generate_user_data


def test_successful_registration(driver):
    # Start auf der Homepage
    driver.get(BASE_URL)
    home_page = HomePage(driver)

    # Navigation zum Login
    home_page.go_to_login()

    # Navigation zur Registrierung
    login_page = LoginPage(driver)
    login_page.go_to_create_account()

    # Name, Mail, Password eintippen
    user = generate_user_data()
    registration_page = RegistrationPage(driver)
    registration_page.registration(user["name"], user["email"], user["password"])

    # Erfolgsmeldung abfangen und prüfen
    success_message = login_page.find(login_page.SUCCESS_MESSAGE)
    assert "Registration successful." in success_message.text