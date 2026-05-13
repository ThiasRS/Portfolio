from selenium.webdriver.common.by import By
from pages.base_page import BasePage

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