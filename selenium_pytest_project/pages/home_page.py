from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    LOGIN_LINK = (By.XPATH, "//a[text()='Sign In']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Register']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Log Out']")
    ACCOUNT_BUTTON = (By.CLASS_NAME, "headerIcon")
    SHOP_BUTTON = (By.XPATH, "(//a[@href='/store'])[1]")

    def go_to_login(self):
        """Aktion: Klicke auf Sign In, um zur Login-Seite zu gelangen."""
        self.click(self.LOGIN_LINK)

    def click_account_button(self):
        self.click(self.ACCOUNT_BUTTON)

    def go_to_shop(self):
        self.click(self.SHOP_BUTTON)