from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest


def handle_cookies(driver):
    try:
        # Wartestrategie
        wait = WebDriverWait(driver, 5)
        # Cookie Button klicken sobald es auftaucht.
        cookie_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".fc-primary-button")))
        cookie_button.click()
        print("Cookies akzeptiert.")
    except:
        print("Kein Cookie-Banner erschienen.")


def register_automation(user, mail):
    # 1. Browser starten
    driver = webdriver.Chrome()
    # 2. Zur URL navigieren
    driver.get("https://automationexercise.com//")
    # Cookies akzeptieren (Extra-Schritt)
    handle_cookies(driver)
    # 3. Wartestrategie und Prüfung ob Startseite (Home-Button) sichtbar ist
    wait = WebDriverWait(driver, 100)
    wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "fa-home")))
    # 4. Sign-Up Button finden und klicken
    driver.find_element(By.CLASS_NAME, "fa-lock").click()
    # 5. Wartestrategie und Prüfung ob 'New User Signup!' sichtbar ist
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".signup-form h2")))
    # 6. Username-/Mail Box finden und Werte eingeben
    driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-name"]').send_keys(user)
    driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-email"]').send_keys(mail)
    # 7. Signup Button finden und klicken
    driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-button"]').click()
    # 8. Wartestrategie und prüfen ob 'ENTER ACCOUNT INFORMATION' sichtbar ist
    wait.until(
        expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".login-form h2 b"),
            "ENTER ACCOUNT INFORMATION"
        )
    )
    # 9. Elemente Titel, Passwort, Geburtsdatum finden und ausfüllen. (Name und Mail vorausgefüllt)
    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.ID, "password").send_keys("testpassword")
    driver.find_element(By.ID, "days").send_keys("24")
    driver.find_element(By.ID, "months").send_keys("August")
    driver.find_element(By.ID, "years").send_keys("1993")
    # 10. Kontrollkästchen anklicken für newsletter
    driver.find_element(By.ID, "newsletter").click()
    # 11. Kontrollkästchen anklicken für special offers
    driver.find_element(By.ID, "optin").click()
    # 12. Details ausfüllen
    user_details = {
        "first_name": "Max",
        "last_name": "Mustermann",
        "company": "Test GmbH",
        "address1": "Hauptstraße 1",
        "address2": "Hinterhaus",
        "state": "NRW",
        "city": "Berlin",
        "zipcode": "12345",
        "mobile_number": "01701234567"
    }
    for key, value in user_details.items():
        driver.find_element(By.ID, f"{key}").send_keys(value)
    driver.find_element(By.ID, "country").send_keys("Australia")
    # 13. 'Create Account' anklicken
    driver.find_element(By.CLASS_NAME, "btn-default").click()
    # 14. Wartestrategie und prüfen ob 'ACCOUNT CREATED!' sichtbar ist
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[data-qa="account-created"]')))
    # 15. Auf 'Continue' klicken
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    # Seite neu laden um Werbung zu umgehen (Extra-Schritt)
    driver.refresh()
    driver.get("https://automationexercise.com/")
    # 16. Wartestrategie und prüfen ob 'Logged in as username' sichtbar ist
    wait.until(
        expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "li:nth-child(10) a"),  # Manche Browser unterstützen das nicht perfekt
            f"Logged in as {user}"
        )
    )
    # 17. Button 'Delete Account' finden und klicken
    driver.find_element(By.CLASS_NAME, "fa-trash-o").click()
    # 18. Wartestrategie, Prüfen ob 'ACCOUNT DELETED!' sichtbar ist und auf 'Continue' klicken
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[data-qa="account-deleted"]')))
    driver.find_element(By.CLASS_NAME, "btn-primary").click()






    print("Registrierung und Account Löschung erfolgreich!")

register_automation("testuser12", "test12@mail.de")