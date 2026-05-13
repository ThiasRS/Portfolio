from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='Street Address']")
    CITY_FIELD = (By.XPATH, "//input[@placeholder='City']")
    POSTAL_CODE_FIELD = (By.XPATH, "//input[@placeholder='Postal Code']")
    CARD_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='Card number']")
    NAME_CARD_FIELD = (By.XPATH, "//input[@placeholder='Name on card']")
    EXPIRATION_FIELD = (By.XPATH, "//input[@placeholder='Expiration']")
    CVV_FIELD = (By.XPATH, "//input[@placeholder='Cvv']")
    BUY_NOW_BUTTON = (By.XPATH, "//button[@class='btn-buy-now']")

    def fill_out_shipment_payment_information(self, data):
        # Adresse und Ort
        self.type(self.ADDRESS_FIELD, data["street"])
        self.type(self.CITY_FIELD, data["city"])
        self.type(self.POSTAL_CODE_FIELD, data["zip"])

        # Kreditkarten-Infos
        self.type(self.CARD_NUMBER_FIELD, data["card_number"])
        self.type(self.NAME_CARD_FIELD, data["card_name"])
        self.type(self.EXPIRATION_FIELD, data["expiration"])
        self.type(self.CVV_FIELD, data["cvv"])

    def click_buy_now_button(self):
        self.click(self.BUY_NOW_BUTTON)

