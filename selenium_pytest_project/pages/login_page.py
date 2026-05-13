from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    EMAIL_FIELD = (By.XPATH, "//input[@type='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.CLASS_NAME, "submit-btn")
    LOGOUT_BUTTON = (By.CLASS_NAME, "logout-btn")


    def login(self, email, password):
        """Führt den kompletten Login-Prozess aus."""
        self.type(self.EMAIL_FIELD, email)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)


    def click_account_button(self):
        self.click(self.ACCOUNT_BUTTON)


    def check_logout_visible(self):
        # 1. Erstmal nur im DOM finden (ohne Sichtbarkeits-Zwang)
        element = self.wait.until(EC.presence_of_element_located(self.LOGOUT_BUTTON))

        # 2. Den Fokus per Selenium-Befehl setzen (das löst oft das Scrollen aus)
        # Wir schicken eine "leere" Taste an das Element
        try:
            element.send_keys("")
        except:
            # Falls das Element kein Eingabefeld ist, ignorieren wir den Fehler
            pass

        # 3. Jetzt prüfen, ob deine find-Methode es sieht
        return self.find(self.LOGOUT_BUTTON).is_displayed()