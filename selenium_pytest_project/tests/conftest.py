import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()

    # 1. Passwort-Manager & Autofill komplett blockieren
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,  # Blockiert Benachrichtigungen
        "autofill.profile_enabled": False,  # Blockiert Adress-Autofill
        "autofill.credit_card_enabled": False  # Blockiert Zahlungsdaten
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # 2. Inkognito-Modus (Das ist oft der Gamechanger!)
    # Im Inkognito-Modus speichert Chrome keine Passwörter und fragt seltener nach
    chrome_options.add_argument("--incognito")

    # 3. Infobars ausschalten
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    yield driver
    driver.quit()