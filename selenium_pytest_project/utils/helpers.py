import random
import string
from faker import Faker
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.constants import BASE_URL

fake = Faker('de_DE')


def generate_text_of_length(length):
    """Erzeugt einen zufälligen String einer bestimmten Länge."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_user_data():
    """Generiert ein Dictionary mit zufälligen Benutzerdaten."""
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password(length=12, special_chars=True, digits=True, upper_case=True)
    }


def register_and_login_new_user(driver):
    # Homepage aufrufen
    driver.get(BASE_URL)
    home_page = HomePage(driver)

    # LoginPage aufrufen und zur Registrierung navigieren
    home_page.go_to_login()
    login_page = LoginPage(driver)
    login_page.go_to_create_account()

    # Registrierung
    user = generate_user_data()
    registration_page = RegistrationPage(driver)
    registration_page.registration(user["name"], user["email"], user["password"])

    # Warten auf Erfolgsmeldung
    login_page.find(login_page.SUCCESS_MESSAGE)

    # Login mit dem registrierten neuen Nutzer
    login_page = LoginPage(driver)
    login_page.login(user["email"], user["password"])

