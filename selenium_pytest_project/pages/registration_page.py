from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    FULL_NAME_FIELD = (By.XPATH, "//input[@type='text']")
    EMAIL_FIELD = (By.XPATH, "//input[@type='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    SIGN_UP_BUTTON = (By.XPATH, "//button[@class='submit-btn']")


    def registration(self, full_name, email, password):
        """Führt den kompletten Login-Prozess aus."""
        self.type(self.FULL_NAME_FIELD, full_name)
        self.type(self.EMAIL_FIELD, email)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.SIGN_UP_BUTTON)
