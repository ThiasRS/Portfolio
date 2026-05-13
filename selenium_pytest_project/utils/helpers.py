import random
import string
from faker import Faker


def generate_text_of_length(length):
    """Erzeugt einen zufälligen String einer bestimmten Länge."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

fake = Faker('de_DE')

def generate_user_data():
    """Generiert ein Dictionary mit zufälligen Benutzerdaten."""
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password(length=12, special_chars=True, digits=True, upper_case=True)
    }


