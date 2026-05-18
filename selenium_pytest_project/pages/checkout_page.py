from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.constants import SHIPPING_FREE

class CheckoutPage(BasePage):
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='Street Address']")
    CITY_FIELD = (By.XPATH, "//input[@placeholder='City']")
    POSTAL_CODE_FIELD = (By.XPATH, "//input[@placeholder='Postal Code']")
    CARD_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='Card number']")
    NAME_CARD_FIELD = (By.XPATH, "//input[@placeholder='Name on card']")
    EXPIRATION_FIELD = (By.XPATH, "//input[@placeholder='Expiration']")
    CVV_FIELD = (By.XPATH, "//input[@placeholder='Cvv']")
    BUY_NOW_BUTTON = (By.XPATH, "//button[@class='btn-buy-now']")
    PRODUCTS_TOTAL_PRICE = (By.XPATH, "(//h5[@class='fw-bold mb-0'])[4]")
    PAGE_BODY = (By.TAG_NAME, "body")

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


    def calculate_difference_till_free_shipping(self):
        """Errechnet den Differenzbetrag bis zum kostenlosen Versand."""
        # 1. Den Text aus dem Element holen (z. B. "14.90€")
        price_text = self.find(self.PRODUCTS_TOTAL_PRICE).text

        # 2. Text säubern, damit Python damit rechnen kann
        # Entfernt das €-Zeichen und Leerzeichen
        cleaned_price = price_text.replace("€", "").strip()

        # 3. In eine Fließkommazahl (Float) umwandeln
        current_total = float(cleaned_price)

        # 4. Differenz berechnen
        if current_total >= SHIPPING_FREE:
            return 0.00  # Versandkosten sind bereits frei
        else:
            # Berechnung der Differenz und runden auf 2 Nachkommastellen
            difference = SHIPPING_FREE - current_total
            return round(difference, 2)

    def is_difference_amount_displayed(self):
        """Prüft, ob der errechnete Differenzbetrag auf der aktuellen Seite sichtbar ist."""
        # 1. Betrag berechnen lassen
        differenz = self.calculate_difference_till_free_shipping()

        # 2. Den Text der Seite über den Locator holen
        page_text = self.find(self.PAGE_BODY).text

        # 3. Die beiden erlaubten Punkt-Formate bauen
        variante_kurz = str(differenz)  # z. B. "19.3"
        variante_lang = f"{differenz:.2f}"  # z. B. "19.30"

        # 4. Rückgabe: True, wenn eins davon im Text existiert, sonst False
        return (variante_kurz in page_text) or (variante_lang in page_text)