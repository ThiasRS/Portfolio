from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    TEXT_AREA = (By.XPATH, "//textarea")
    ERROR_MSG = (By.XPATH, "//p[@class='error-message']")
    INVALID_INPUT_MSG = (By.XPATH, "//div[@role='status']")
    REVIEW_SEND_BTN = (By.XPATH, "//button[@class='new-review-btn new-review-btn-send']")


    def write_product_review(self, review_text):
        self.type(self.TEXT_AREA, review_text)


    def click_review_send_button(self):
        self.click(self.REVIEW_SEND_BTN)