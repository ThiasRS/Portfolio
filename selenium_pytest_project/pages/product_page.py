from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    TEXT_AREA = (By.XPATH, "//textarea")
    ERROR_MSG = (By.XPATH, "//p[@class='error-message']")


    def write_product_review(self, review_text):
        self.type(self.TEXT_AREA, review_text)