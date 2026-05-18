import random
from faker import Faker
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.constants import BASE_URL

fake = Faker('de_DE')


def generate_random_string(length):
    """Generiert einen zufälligen Text mit einer exakten Zeichenlänge"""
    return fake.lexify(text="?" * length)


def generate_user_data():
    """Generiert ein Dictionary mit zufälligen Benutzerdaten."""
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password(length=12, special_chars=True, digits=True, upper_case=True)
    }


def generate_payment_and_address_data():
    """Generiert zufällige Adress- und Zahlungsdaten"""

    # Expiration Date generieren (MM/YY format, in der Zukunft)
    month = f"{random.randint(1, 12):02d}"
    year = random.randint(2026, 2030) # Jahre 2026 bis 2030

    return {
        "street": fake.street_address(),
        "city": fake.city(),
        "zip": fake.postcode(),
        "card_number": fake.credit_card_number(card_type='visa'),  # oder 'mastercard'
        "card_name": fake.name(),
        "expiration": f"{month}/{year}",
        "cvv": fake.credit_card_security_code()
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

