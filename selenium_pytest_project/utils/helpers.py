import random
import string


def generate_text_of_length(length):
    """Erzeugt einen zufälligen String einer bestimmten Länge."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


