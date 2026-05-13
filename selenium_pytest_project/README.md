# Projekt: Test Automatisierung - GroceryMate

Dieses Projekt ist die automatisierte Umsetzung der Testfälle für das System **GroceryMate**. Es basiert auf dem vorangegangenen Testplan und Testfallentwurf. Ziel ist die vollständige Automatisierung der drei neuen Features unter Einhaltung moderner Software-Testing-Prinzipien.

## 🚀 Features & Anforderungen
- **Page Object Model (POM):** Strikte Trennung zwischen Testlogik und Seiteninteraktion.
- **Fixture-Management:** Zentraler Webdriver-Setup in `conftest.py`.
- **Wiederverwendbarkeit:** Vermeidung von Code-Duplizierung durch Basis-Klassen und Hilfsfunktionen.
- **Datengetriebenes Testen:** Parametrisierte Tests für verschiedene Datensets.
- **Reporting:** Erstellung detaillierter Testberichte.
- **Wait-Strategien:** Nutzung von impliziten/expliziten Waits innerhalb der Page Objects.

## 🛠️ Technologien
- **Sprache:** Python
- **Framework:** Pytest
- **Tool:** Selenium WebDriver
- **IDE:** PyCharm

## 📂 Projektstruktur
Die Struktur folgt dem Industriestandard für Selenium-Projekte:

```text
selenium_pytest_project/
│
├── tests/                          # Test-Skripte
│   ├── test_login.py               # Tests für Login-Funktionalität
│   ├── test_registration.py        # Tests für Registrierung
│   └── conftest.py                 # PyTest Fixtures (WebDriver Setup)
│
├── pages/                          # Page Object Model (POM)
│   ├── base_page.py                # Gemeinsame Methoden (Waits, Klicks)
│   ├── login_page.py               # Elemente & Aktionen der Login-Seite
│   └── registration_page.py        # Elemente & Aktionen der Registrierung
│
├── utils/                          # Hilfsmodule & Konfiguration
│   ├── constants.py                # URLs, Credentials, Timeouts (Kein Hardcoding!)
│   └── helpers.py                  # Wiederverwendbare Utility-Funktionen
│
├── screenshots/                    # Screenshots bei Testfehlern
├── reports/                        # Generierte