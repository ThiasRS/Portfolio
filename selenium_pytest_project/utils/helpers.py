import random
from faker import Faker
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.constants import BASE_URL
from datetime import datetime, timedelta

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


def generate_underage_birthday():
    """
    Generiert ein Geburtsdatum, das genau 1 Tag vor dem 18. Geburtstag liegt.
    Format: DD-MM-YYYY
    """
    # 1. Das heutige Datum holen
    today = datetime.now()

    # 2. Berechnen, wann der 18. Geburtstag wäre (heute vor 18 Jahren)
    # Da Schaltjahre die Berechnung mit reinen Tagen ungenau machen,
    # ersetzen wir einfach das Geburtsjahr durch (aktuelles Jahr - 18)
    try:
        eighteen_years_ago = today.replace(year=today.year - 18)
    except ValueError:
        # Falls heute der 29. Februar ist und vor 18 Jahren kein Schaltjahr war
        eighteen_years_ago = today.replace(year=today.year - 18, day=28)

    # 3. Genau 1 Tag HINZUFÜGEN (damit die Person 1 Tag jünger/unter 18 ist)
    birthday = eighteen_years_ago + timedelta(days=1)

    # 4. Im Format DD-MM-YYYY zurückgeben
    return birthday.strftime("%d-%m-%Y")

