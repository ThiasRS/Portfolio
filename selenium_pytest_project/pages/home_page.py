from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Diese Locators gibt es NUR auf der Home Page
    LOGIN_LINK = (By.XPATH, "//a[text()='Sign In']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Register']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Log Out']")
    ACCOUNT_BUTTON = (By.CLASS_NAME, "headerIcon")

    def go_to_login(self):
        """Aktion: Klicke auf Login, um zur Login-Seite zu gelangen."""
        self.click(self.LOGIN_LINK)

    def click_account_button(self):
        self.click(self.ACCOUNT_BUTTON)