import pytest
import os
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


# Hook, um das Ergebnis jedes einzelnen Tests abzufangen
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    # Wir prüfen, ob der Test im "call"-Schritt (also während der Ausführung) fehlgeschlagen ist
    if report.when == "call" and report.failed:
        # Zugriff auf den WebDriver aus dem Test holen
        driver = item.funcargs.get("driver")
        if driver:
            # Ordner für Screenshots erstellen, falls er nicht existiert
            os.makedirs("berichte/screenshots", exist_ok=True)
            screenshot_name = f"berichte/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_name)

            # Den Screenshot relativ zum Bericht verlinken (damit das HTML ihn findet)
            relative_path = f"screenshots/{item.name}.png"
            html = f'<div><img src="{relative_path}" alt="Screenshot bei Fehler" style="width:300px;height:auto;" ' \
                   f'onclick="window.open(this.src)" align="right"/></div>'
            extra.append(item.config.pluginmanager.getplugin("html").extras.html(html))
            report.extra = extra


# Übersetzt die Tabellenköpfe im HTML-Bericht auf Deutsch
def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Beschreibung / Testfall</th>")
    cells.insert(2, "<th>Ergebnis</th>")
    cells.pop(3)  # Entfernt das englische "Result"
    cells.pop()  # Entfernt "Links" falls nicht benötigt


# Befüllt die deutschen Spalten mit den passenden Daten
def pytest_html_results_table_row(report, cells):
    # Liest den Docstring (dreifache Anführungszeichen) des Tests als Beschreibung aus
    description = report.description if hasattr(report, "description") else ""
    if report.longrepr:
        # Falls vorhanden, nutzen wir den Docstring des Tests
        description = report.nodeid.split("::")[-1]

    cells.insert(1, f"<td>{description}</td>")

    # Ergebnis auf Deutsch übersetzen
    status = "BESTANDEN" if report.passed else "FEHLGESCHLAGEN" if report.failed else "ÜBERSPRUNGEN"
    color = "green" if report.passed else "red" if report.failed else "orange"

    cells.insert(2, f"<td style='color: {color}; font-weight: bold;'>{status}</td>")
    cells.pop(3)
    cells.pop()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    # Hilfs-Hook, um Beschreibungen aus den Tests für die Tabelle zu sichern
    if report.when == "call":
        report.description = report.nodeid.split("::")[-1]