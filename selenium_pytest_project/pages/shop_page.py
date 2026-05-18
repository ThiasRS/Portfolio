from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ShopPage(BasePage):
    FIRST_PRODUCT_ADD_TO_CART = (By.XPATH, "(//button[text()='Add to Cart'])[1]")
    FIRST_PRODUCT = (By.XPATH, "(//div[@class='card-header'])[1]")
    CART_BUTTON = (By.XPATH, "(//div[@class='headerIcon'])[3]")
    CONFIRM_AGE_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    BIRTHDAY_FIELD = (By.XPATH, "//input[@placeholder='DD-MM-YYYY']")
    ALCOHOL_SHOP_CATEGORY = (By.XPATH, "//a[text()='Alocohol']")
    UNDERAGE_NOTICE = (By.XPATH, "//h2[text()='Underage Notice']")

    def add_first_product_to_cart(self):
        self.click(self.FIRST_PRODUCT_ADD_TO_CART)


    def click_cart_button(self):
        self.click(self.CART_BUTTON)


    def skip_age_verification(self):
        self.click(self.CONFIRM_AGE_BUTTON)


    def click_first_product(self):
        self.click(self.FIRST_PRODUCT)


    def age_verification(self, birthday):
        self.type(self.BIRTHDAY_FIELD, birthday)
        self.click(self.CONFIRM_AGE_BUTTON)


    def navigate_to_alcohol_category(self):
        self.click(self.ALCOHOL_SHOP_CATEGORY)